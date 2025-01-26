% Labb2 3a)
clear, clc
fprintf('\n--------------------------------------- a) ----------------------------------------\n\n')

% Parametrar
L = 4;             % Längd på stav
k = 2.2;           % Värmeledningsförmåga
t0 = 290;          % Temperatur vid x = 0
t1 = 400;          % Temperatur vid x = L
n = 20;            % Antalet inre punkter (kan ändras)
h = L / (n + 1);   % Steglängd, beräknas som längden dividerad med antalet punkter
xj = 3;            % En specifik position (kan ändras beroende på behov)

% Diskretisera x och beräkna Q(x) för varje xi
xi = linspace(0, L, n+2);                            % Skapar en linjär fördelning av n+2 punkter inklusive ändpunkterna 0 och L
Q = @(x) 3000 * exp(-20 * (x - 0.6 * L).^2) + 200;   % Funktion för värmekällans intensitet beroende på x

% Konstruera matrisen A som representerar den diskretiserade differentialekvationen
main_diag = 2 * ones(n, 1);  % Huvuddiagonalen 
off_diag = -1 * ones(n-1, 1);  % Bortre diagonalen 
A = (diag(main_diag) + diag(off_diag, 1) + diag(off_diag, -1));  % Skapa matrisen A genom: diag(v) och diag(v,p)

% Konstruera vektorn b som motsvarar värmekällans inverkan och randvillkor
b = (h^2 / k) * Q(xi(2:end-1)');  % Värden på vektorn b beräknas från funktionen Q för de inre punkterna
b(1) = b(1) + t0;  % Justera första elementet i b för randvillkoret T0 = t0
b(end) = b(end) + t1;  % Justera sista elementet i b för randvillkoret Tn+1 = t1

disp('Matris A:');  
disp(A);
disp('Vektor b:');  
disp(b);


%% Labb2 3b)
fprintf('--------------------------------------- b) ----------------------------------------\n\n')

% Lös systemet och beräkna hela temperaturprofilen
T_inre = A \ b;  % Lös systemet A * T_inre = b för att få de inre temperaturerna
T = [t0; T_inre; t1];  % Lägg till randvillkor (t0 och t1) till den inre lösningen
figure;  
plot(xi, T, '-o');  
xlabel('x (m)');  
ylabel('Temperatur T (K)'); 
title('Temperatur som funktion av position x');  
grid on; 

% Funktion för att beräkna temperatur vid en specifik position xj
function T_x = temper(L, k, t0, t1, n, xj)
    h = L / (n + 1);  % Beräkna steglängden
    xi = linspace(0, L, n+2);  % Skapa en linjär fördelning av n+2 punkter inklusive ändpunkterna 0 och L
    Q = @(x) 3000 * exp(-20 * (x - 0.6 * L).^2) + 200;  % Funktion för värmekällans intensitet beroende på x

    main_diag = 2 * ones(n, 1);  
    off_diag = -1 * ones(n-1, 1);  
    A = sparse(diag(main_diag) + diag(off_diag, 1) + diag(off_diag, -1)); 

    b = (h^2 / k) * Q(xi(2:end-1)'); 
    b(1) = b(1) + t0;  
    b(end) = b(end) + t1;  % Justera sista elementet i b för randvillkoret Tn+1 = t1

    T_inre = A \ b;  % Lös systemet A * T_inre = b för att få de inre temperaturerna
    T = [t0; T_inre; t1];  % Lägg till randvillkor (t0 och t1) till den inre lösningen
    [~, j] = min(abs(xi - xj));  % Hitta index j* för närmaste x-värde till xj
    T_x = T(j);  % Hämta temperaturvärdet vid xj*
end

% Beräkna temperaturen vid x = 3
T_19 = temper(L, k, t0, t1, n-1, xj);  % Anropa funktionen för att beräkna temperaturen vid xj
fprintf('Temperaturen vid x = %.1f är T(x) = %.4f K\n\n', xj, T_19); 



%% Labb2 3c)
fprintf('--------------------------------------- c) ----------------------------------------\n\n')

tolerans = 0.5e-5; 
niter_T = 0;  
n_T = n;  
fel_T = tolerans + 1;  

fprintf('n\t\t T(3)\t\t\t\t Feldifferenser\n');  

T_prev = 0;  % Föregående temperaturvärde, används för att beräkna differensen
while fel_T > tolerans  
    T_curr = temper(L, k, t0, t1, n_T-1, xj);  % Beräkna temperatur för aktuellt n
    if niter_T > 0
        fel_T = abs(T_curr - T_prev);  % Beräkna skillnaden mellan föregående och nuvarande temperatur
    end
    
    % Skriv ut resultatet för den aktuella iterationen
    if niter_T == 0
        fprintf('%d\t\t %.10f\t\t N/A\n', n_T-1, T_curr);  % Första iterationen har ingen diff
    else
        fprintf('%d\t\t %.10f\t\t %.10f\n', n_T-1, T_curr, -fel_T);  % Skriv ut temperatur och differens
    end
    
    T_prev = T_curr;  % Uppdatera temperaturvärdet för nästa iteration
    niter_T = niter_T + 1;  
    n_T = n_T * 2; 
end

fprintf('\nTemperaturen för x = 3 med fem korrekta decimaler är: %.5f\n\n', T_curr);  


% Initiera listor och startvärden för kvot och noggrannhet
kvot_T = [];
noggrann_lista = [];
n_T = n;  % Startvärde för n
T_2h = temper(L, k, t0, t1, n_T-1, xj);  

fprintf('n\t\t\t Kvot\t\t\t Noggrannhetsrdning\n');  

for j = 0:6  
    % Beräkna temperaturen med dubbelt så många punkter
    T_h = temper(L, k, t0, t1, n_T-1, xj);  % Beräkna temperatur med nuvarande n_T
    
    % Beräkna kvot och noggrannhetsordning om möjligt
    if j > 1  % Börja beräkna kvot och noggrannhet från tredje iterationen
        kvot = (T_4h - T_2h) / (T_2h - T_h);  
        noggrann = log2(kvot);  
        kvot_T = [kvot_T, kvot];  
        noggrann_lista = [noggrann_lista, noggrann];  
        
        fprintf('%d\t\t\t %.5f\t\t %.5f\n', n_T-1, kvot, noggrann);  % Skriv ut resultatet för den aktuella iterationen
    else
        fprintf('%d\t\t\t N/A\t\t\t N/A\n', n_T-1);  % Första iterationerna saknar kvot och noggrannhet
    end
    
    % Uppdatera temperaturvärden för nästa iteration
    T_4h = T_2h;  
    T_2h = T_h;  
    n_T = n_T * 2; 
end
