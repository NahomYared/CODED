% Labb2 1a)
clear, clc
fprintf('\n--------------------------------------- a) ----------------------------------------\n\n')

% Konstanter och parametrar
R = 3;                   % Radie
Ka = [0,R];              % Intervall [a, b]
n = 30;                  % Antal delintervall
tolerans = 0.5e-4;       % Tolerans för konvergens

% Funktioner som används i beräkningen
g = @(r) 3 .* r.^3 .* exp(-r) ./ (1 + (1/3) * sin(8 * r / 5)); 
f = @(r) g(r) .* r;                                            

% Exakt volym vid ytan, används som referens
v0 = g(R) * R^2 * pi;

% Funktion för att beräkna integral med trapetsmetoden
function T = trapets(f, R, Ka, n)
    h = R / n;               % Steglängd
    x = Ka(1):h:Ka(2);       % Diskreta punkter inom intervallet
    y = f(x);                % Funktionens värden vid dessa punkter
    % Trapetsmetodens formel
    T = h * (0.5 * y(1) + sum(y(2:end-1)) + 0.5 * y(end));
end

% Funktion för att beräkna integral med Simpsons metod
function S = simpsons(f, R, Ka, n)
    % Kontrollera att n är jämnt (krav för Simpsons regel)
    if mod(n, 2) ~= 0
        error('Antal delintervall n måste vara jämnt för Simpsons regel.');
    end
    h = R / n;               
    x = Ka(1):h:Ka(2);       
    y = f(x);                
    % Simpsons metods formel
    S = h / 3 * (y(1) + 4 * sum(y(2:2:end-1)) + 2 * sum(y(3:2:end-2)) + y(end));
end

% Beräkning av volymer med n och 2n delintervall för båda metoderna
T30 = v0 - 2 * pi * trapets(f, R, Ka, n);
T60 = v0 - 2 * pi * trapets(f, R, Ka, n*2);
S30 = v0 - 2 * pi * simpsons(f, R, Ka, n);
S60 = v0 - 2 * pi * simpsons(f, R, Ka, n*2);

fprintf('Volymen beräknad med trapetsregeln (n=%d): %.8f\n', n, T30);
fprintf('Volymen beräknad med trapetsregeln (n=%d): %.8f\n\n', n*2, T60);
fprintf('Volymen beräknad med Simpsons formel (n=%d): %.8f\n', n, S30);
fprintf('Volymen beräknad med Simpsons formel (n=%d): %.8f\n\n', n*2, S60);

% Initiera listor och iterationsräknare för Trapets- och Simpsonsmetoderna
Trapets_lista = [];
Simpsons_lista = [];
niter_T = 0;
niter_S = 0;

% Iterativ beräkning med trapetsregeln tills toleransen uppnås
for i = 0:20
    Tn = v0 - 2 * pi * trapets(f, R, Ka, n*2^i); 
    Trapets_lista = [Trapets_lista, Tn];        
    niter_T = niter_T + 1;                      
    
    if i > 0 && norm(Trapets_lista(end)-Trapets_lista(end-1)) < tolerans
        break
    end
end

% Beräkna antal intervall och steglängd för Trapetsmetoden
nT = 30*2^(niter_T - 1);
hT = diff(Ka)/nT;

% Iterativ beräkning med Simpsons regel tills toleransen uppnås
for i = 0:30
    Sn = v0 - 2 * pi * simpsons(f, R, Ka, n*2^i); 
    Simpsons_lista = [Simpsons_lista, Sn];       
    niter_S = niter_S + 1;                       
   
    if i > 0 && norm(Simpsons_lista(end)-Simpsons_lista(end-1)) < tolerans
        break
    end
end

% Beräkna antal intervall och steglängd för Simpsons metoden
nS = 30*2^(niter_S - 1);
hS = diff(Ka)/nS;

fprintf('Trapetsregeln med 4 korrekta decimaler ger volymen: %.4f uppnåddes vid steglängden h = %.10f eller %.d intervall\n', Trapets_lista(end), hT, nT);
fprintf('Simpsons formel med 4 korrekta decimaler ger volymen: %.4f uppnåddes vid steglängden h = %.10f eller %.d intervall\n\n', Simpsons_lista(end), hS, nS);
fprintf('Felet för: \nTrapetsregeln: %.5f\nSimpsons formel: %.5f\n\n', norm(T30-T60), norm(S30-S60));
fprintf('--------------------------------------- b) ----------------------------------------\n\n');




% Labb2 1b)

L = 3 * sqrt(2);        % Längd för kvadratens sida i 2D-integrationen
tolerans2 = 0.5e-3;     

% Intervall i x- och y-led för 2D-integrationen
Kbx = [-L/2, L/2];      
Kby = [-L/2, L/2];      

% Funktion att integrera i 2D
f2 = @(x, y) g(R) - g(sqrt(x^2 + y^2)); % Funktion baserad på avstånd från origo

% Funktion för dubbel integral med trapetsmetoden
function T = trapets2D(Kbx, Kby, f, m, n)
    
    hx = diff(Kbx) / m;  % Steglängd i x-led
    hy = diff(Kby) / n;  % Steglängd i y-led
    Tn = 0;              % Initiera summan för volymberäkning

    % Iterera över alla delintervall i x- och y-led
    for i = 0:m
        for j = 0:n
            x = Kbx(1) + i * hx; % x-koordinat
            y = Kby(1) + j * hy; % y-koordinat
            
            % Viktfaktor för trapetsmetoden i 2D
            if (i == 0 || i == m) && (j == 0 || j == n)
                w = 1;    % Hörnpunkter
            elseif (i == 0 || i == m) || (j == 0 || j == n)
                w = 2;    % Kantpunkter
            else
                w = 4;    % Inre punkter
            end
            
            % Summera med viktning
            Tn = Tn + w * f(x, y);
        end
    end
    
    % Multiplicera med steglängd och viktning för att få slutlig integral
    T = (hx * hy / 4) * Tn;
end

% Beräkning av volym med n och 2n delintervall i båda riktningarna
T30_2D = trapets2D(Kbx, Kby, f2, n, n);
T60_2D = trapets2D(Kbx, Kby, f2, n*2, n*2);

fprintf('Trapetsregeln för dubbelintegralen(2D) n=30 ger volymen: %.5f\n', T30_2D);
fprintf('Trapetsregeln för dubbelintegralen(2D) n=60 ger volymen: %.5f\n\n', T60_2D);

Trapets2D_lista = [];
niter_T2D = 0;

for i = 0:20
    Volym_Tn = trapets2D(Kbx, Kby, f2, 30*2^i, 30*2^i); 
    Trapets2D_lista = [Trapets2D_lista, Volym_Tn];     
    niter_T2D = niter_T2D + 1;                         
    
    if i > 0 && norm(Trapets2D_lista(end) - Trapets2D_lista(end-1)) < tolerans2
        break
    end
end

intervall_Tn = 30 * 2^(niter_T2D - 1); % Totalt antal intervall
h_bx = diff(Kbx) / intervall_Tn;       % Steglängd i x-led
h_by = diff(Kby) / intervall_Tn;       % Steglängd i y-led

fprintf(['Trapetsregeln för dubbelintegralen(2D) med 3 korrekta decimaler ger volymen: %.4f ' ...
    '\nUpnåddes vid:\nx-steglängden h = %.10f & y-steglängden h = %.10f \n' ...
    'eller \n%.d x-intervall och %.d y-intervall\n\n'], ...
    Trapets2D_lista(end), h_bx, h_by, intervall_Tn, intervall_Tn);

fprintf('--------------------------------------- c) ----------------------------------------\n\n');




% Labb2 1c) #metod 1


lista_felet_trapets = [];   % Lista för att spara approximationsfelen för Trapetsmetoden
lista_h_trapets = [];       % Lista för att spara steglängder för Trapetsmetoden
niter_Tn = n;               % Startvärde för antal delintervall

% Referensvärde med hög noggrannhet (Simpsons)
referens_S = v0 - 2 * pi * simpsons(f, R, Ka, 30*(2^6));

% Iterativ beräkning för Trapetsmetoden
for i = 1:5
    varde_T = v0 - 2 * pi * trapets(f, R, Ka, niter_Tn);  % Beräknar volymen med Trapetsmetoden
    fel_T = norm(referens_S - varde_T);                   % Approximationsfel: skillnaden mellan referensvärde och nuvarande approximation
    h_T = diff(Ka) / niter_Tn;                            % Steglängd för nuvarande delintervall

    % Spara fel och steglängd
    lista_felet_trapets = [lista_felet_trapets, fel_T];
    lista_h_trapets = [lista_h_trapets, h_T];

    % Fördubbla antal delintervall
    niter_Tn = niter_Tn * 2;
end

% Felberäkning för Simpsons metod
lista_felet_simpsons = [];  
lista_h_simpsons = [];      
niter_Sn = n;               

for i = 1:5
    varde_S = v0 - 2 * pi * simpsons(f, R, Ka, niter_Sn);
    fel_S = norm(referens_S - varde_S);
    h_S = diff(Ka) / niter_Sn;
 
    lista_felet_simpsons = [lista_felet_simpsons, fel_S];
    lista_h_simpsons = [lista_h_simpsons, h_S];

    niter_Sn = niter_Sn * 2;
end

% Referensvärde med hög noggrannhet för Trapetsmetoden i 2D
referens_T2D = trapets2D(Kbx, Kby, f2, 30*(2^6), 30*(2^6));

lista_felet_trapets2D = []; 
lista_h_trapets2D = [];    
niter_T2D = n;              

for i = 1:5
    varde_T2D = trapets2D(Kbx, Kby, f2, niter_T2D, niter_T2D);
    fel_T2D = norm(referens_T2D - varde_T2D);
    hx_T2D = diff(Kbx) / niter_T2D;

    lista_felet_trapets2D = [lista_felet_trapets2D, fel_T2D];
    lista_h_trapets2D = [lista_h_trapets2D, hx_T2D];

    niter_T2D = niter_T2D * 2;
end

figure;         
grid on;       
hold on;        
set(gca, 'XScale', 'log', 'YScale', 'log');
loglog(lista_h_trapets, lista_felet_trapets, 'r--o', 'DisplayName', 'Trapets'); % Trapetsmetoden
loglog(lista_h_simpsons, lista_felet_simpsons, 'b--s', 'DisplayName', 'Simpsons'); % Simpsons regel
loglog(lista_h_trapets2D, lista_felet_trapets2D, 'g--^', 'DisplayName', 'Trapets 2D'); % Trapetsmetoden i 2D
xlabel('Steglängd h'); 
ylabel('Approximationsfelet E(h)');
title('Approximationsfelet för olika metoder');
legend('Location', 'best');
ax = axis;
axis(ax);  




% Labb2 1c) #metod 2

% Felreduktion och noggrannhetsordning för Trapetsmetoden i 1D
kvot_T1D = [];            
p_t1_lista = [];          
n_T1D = 30 * (2^3);       

% Iterativ beräkning för Trapetsmetoden i 1D
for j = 1:5
    % Beräknar volymer för h, 2h, och 4h
    V_h = 2 * pi * trapets(f, R, Ka, n_T1D);      % h = R / n
    V_2h = 2 * pi * trapets(f, R, Ka, n_T1D / 2); % 2h
    V_4h = 2 * pi * trapets(f, R, Ka, n_T1D / 4); % 4h

    % Felreduktionskvot och noggrannhetsordning
    kvot_iter = (V_4h - V_2h) / (V_2h - V_h);   % Uppskattar felreduktionen
    p_t1 = log2(kvot_iter);                     % Noggrannhetsordningen

    kvot_T1D = [kvot_T1D, kvot_iter];
    p_t1_lista = [p_t1_lista, p_t1];

    n_T1D = n_T1D * 2;
end

% Felreduktion och noggrannhetsordning för Simpsons regel i 1D
kvot_S1D = [];            
p_s_lista = [];           
n_S1D = 30 * (2^3);       

for k = 1:5
    
    V_h = 2 * pi * simpsons(f, R, Ka, n_S1D);      
    V_2h = 2 * pi * simpsons(f, R, Ka, n_S1D / 2); 
    V_4h = 2 * pi * simpsons(f, R, Ka, n_S1D / 4); 

    kvot_iter = (V_4h - V_2h) / (V_2h - V_h);
    p_s = log2(kvot_iter);

    kvot_S1D = [kvot_S1D, kvot_iter];
    p_s_lista = [p_s_lista, p_s];

    n_S1D = n_S1D * 2;
end

% Felreduktion och noggrannhetsordning för Trapetsmetoden i 2D
kvot_T2D = [];           
p_t2_lista = [];          
n_T2D = 30 * (2^2);       

% Iterativ beräkning för Trapetsmetoden i 2D
for i = 1:4
    
    V_h = 2 * pi * trapets2D(Kbx, Kby, f2, n_T2D, n_T2D);          % h
    V_2h = 2 * pi * trapets2D(Kbx, Kby, f2, n_T2D / 2, n_T2D / 2); % 2h
    V_4h = 2 * pi * trapets2D(Kbx, Kby, f2, n_T2D / 4, n_T2D / 4); % 4h

    kvot_iter = (V_4h - V_2h) / (V_2h - V_h);
    p_t2 = log2(kvot_iter);

    kvot_T2D = [kvot_T2D, kvot_iter];
    p_t2_lista = [p_t2_lista, p_t2];

    n_T2D = n_T2D * 2;
end

% Skapa tabeller för att sammanställa resultaten
trapets1D_tabell = table(kvot_T1D', p_t1_lista', ...
    'VariableNames', {'Trapets1D, (V4h-V2h)/(V2h-Vh)', 'Noggrannhetsordning'});
simpsons_tabell = table(kvot_S1D', p_s_lista', ...
    'VariableNames', {'Simpsons, (V4h-V2h)/(V2h-Vh)', 'Noggrannhetsordning'});
trapets2D_tabell = table(kvot_T2D', p_t2_lista', ...
    'VariableNames', {'Trapets2D, (V4h-V2h)/(V2h-Vh)', 'Noggrannhetsordning'});

format long;
disp(trapets1D_tabell);
disp(simpsons_tabell);
disp(trapets2D_tabell);







