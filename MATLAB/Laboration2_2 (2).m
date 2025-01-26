%% Labb2 2a) 
clear, clc
fprintf('\n------------------------------ a) --------------------------------\n\n')

% Parametrar
g = 9.81;         % Tyngdacceleration (m/s^2)
m = 0.6;          % Massa (kg)
L = 1.5;          % Längd på pendeln (m)
my = 0.2;         % Dämpningskoefficient
h = 0.025;        % Steglängd för tidsdiskretisering (s)
t = 5;            % Sluttid för simulering (s)
phi0 = 0.5;       % Begynnelsevärde för vinkel φ (rad)
phi_prim0 = 0;    % Begynnelsevärde för vinkelhastighet φ' (rad/s)

% Toleranser 
tol_framateuler = 0.5e-2;  
tol_rungekutta4 = 0.5e-6;  

% Tidvektor
T = 0:h:t; % Vektor med diskreta tidpunkter från 0 till sluttid med steglängd h

[T, Phi_Euler, Phi_prim_Euler] = framat_euler(T, phi0, phi_prim0, h, m, my, g, L);
[T, Phi_RK4, Phi_prim_RK4] = runge_kutta_4(T, phi0, phi_prim0, h, m, my, g, L);

fprintf('φ(5) enligt Framåt Euler: %.6f rad\n', Phi_Euler(end));
fprintf('φ(5) enligt Runge Kutta 4: %.6f rad\n\n', Phi_RK4(end));

figure;
plot(T, Phi_Euler, 'm:', 'linewidth', 1.5, 'DisplayName', 'Framåt Euler'); 
hold on;
plot(T, Phi_RK4, 'k--', 'linewidth', 1, 'DisplayName', 'Runge-Kutta 4');  
legend;                 
xlabel('Tid t');         
ylabel('\phi(t) rad');   
title('Jämförelse av Framåt Euler och Runge-Kutta 4'); 
grid on;                 
hold off;


%% Labb2 2b) 
fprintf('------------------------------ b) --------------------------------\n\n')

% Anropa iterationsfunktionen för Framåt Euler och Runge-Kutta 4
[lista_euler_b, FE_err, h_FE] = iteration(@framat_euler, g, m, L, my, h, t, phi0, phi_prim0, tol_framateuler);
[lista_Rungekutta4_b, RK_err, h_RK] = iteration(@runge_kutta_4, g, m, L, my, h, t, phi0, phi_prim0, tol_rungekutta4);

fprintf('φ(5) med 2 korrekta decimaler för Framåt Euler: %.2f\n', lista_euler_b(end));
fprintf('φ(5) med 6 korrekta decimaler för Runge Kutta 4: %.6f\n\n', lista_Rungekutta4_b(end));

kvotlista_euler = [];
kvotlista_rungekutta4 = [];
h_lista = [];

% Iterera över olika steglängder för att beräkna noggrannheten och kvoter
for i = 1:6
    % Lägg till den nuvarande steglängden i listan
    h_lista = [h_lista, h/(2^i)];

    % Framåt Euler: Beräkna värden med olika steglängder och beräkna kvot
    [~, framateuler_h, ~] = framat_euler(0:h/(2^i):t, phi0, phi_prim0, h/(2^i), m, my, g, L);
    [~, framateuler_2h, ~] = framat_euler(0:2*h/(2^i):t, phi0, phi_prim0, 2*h/(2^i), m, my, g, L);
    [~, framateuler_4h, ~] = framat_euler(0:4*h/(2^i):t, phi0, phi_prim0, 4*h/(2^i), m, my, g, L);
    
    % Beräkna kvoten för Framåt Euler (jämförelse mellan olika steglängder)
    kvot_framateuler = (framateuler_4h(end) - framateuler_2h(end)) / (framateuler_2h(end) - framateuler_h(end));
    kvotlista_euler = [kvotlista_euler, kvot_framateuler];

    % Runge-Kutta 4: Beräkna värden med olika steglängder och beräkna kvot
    [~, rungekutta4_h, ~] = runge_kutta_4(0:h/(2^i):t, phi0, phi_prim0, h/(2^i), m, my, g, L);
    [~, rungekutta4_2h, ~] = runge_kutta_4(0:2*h/(2^i):t, phi0, phi_prim0, 2*h/(2^i), m, my, g, L);
    [~, rungekutta4_4h, ~] = runge_kutta_4(0:4*h/(2^i):t, phi0, phi_prim0, 4*h/(2^i), m, my, g, L);

    % Beräkna kvoten för Runge-Kutta 4 (jämförelse mellan olika steglängder)
    kvot_rungekutta4 = (rungekutta4_4h(end) - rungekutta4_2h(end)) / (rungekutta4_2h(end) - rungekutta4_h(end));
    kvotlista_rungekutta4 = [kvotlista_rungekutta4, kvot_rungekutta4];
end

% Konvertera kvoterna till noggrannhetsordning med log2
noggrannhet_framateuler = log2(abs(kvotlista_euler));
noggrannhet_rungekutta4 = log2(abs(kvotlista_rungekutta4));

fprintf('\n---------------- Noggrannhetsordning ------------------\n\n')
resultat_tabell = table(h_lista', noggrannhet_framateuler', noggrannhet_rungekutta4', ...
    'VariableNames', {'h', 'Framåt Euler', 'Runge Kutta 4'});
disp(resultat_tabell);


%% Labb2 Funktioner

function [T, Phi, Phi_prim] = framat_euler(T, phi0, phi_prim0, h, m, my, g, L)
    % Initialisera lösningsvektorer
    N = length(T);
    Phi = zeros(1, N);       % Vektor för φ
    Phi_prim = zeros(1, N);  % Vektor för φ'
    
    % Begynnelsevärden
    Phi(1) = phi0;
    Phi_prim(1) = phi_prim0;
    
    % Framåt Euler-metoden
    for i = 1:N-1
        Phi_bis = (- (my/m) * Phi_prim(i) - (g/L) * sin(Phi(i)));
        Phi(i+1) = Phi(i) + h * Phi_prim(i);
        Phi_prim(i+1) = Phi_prim(i) + h * Phi_bis;
    end
end

function [T, Phi, Phi_prim] = runge_kutta_4(T, phi0, phi_prim0, h, m, my, g, L)
    % Initialisera lösningsvektorer
    N = length(T);
    Phi = zeros(1, N);       % Vektor för φ
    Phi_prim = zeros(1, N);  % Vektor för φ'
    
    % Begynnelsevärden
    Phi(1) = phi0;
    Phi_prim(1) = phi_prim0;
    
    % Runge-Kutta 4-metoden
    for i = 1:N-1
        k1_phi = Phi_prim(i);
        k1_phi_prim = - (my/m) * Phi_prim(i) - (g/L) * sin(Phi(i));
        
        k2_phi = Phi_prim(i) + 0.5 * h * k1_phi_prim;
        k2_phi_prim = - (my/m) * (Phi_prim(i) + 0.5 * h * k1_phi_prim) - (g/L) * sin(Phi(i) + 0.5 * h * k1_phi);
        
        k3_phi = Phi_prim(i) + 0.5 * h * k2_phi_prim;
        k3_phi_prim = - (my/m) * (Phi_prim(i) + 0.5 * h * k2_phi_prim) - (g/L) * sin(Phi(i) + 0.5 * h * k2_phi);
        
        k4_phi = Phi_prim(i) + h * k3_phi_prim;
        k4_phi_prim = - (my/m) * (Phi_prim(i) + h * k3_phi_prim) - (g/L) * sin(Phi(i) + h * k3_phi);
        
        Phi(i+1) = Phi(i) + (h/6) * (k1_phi + 2*k2_phi + 2*k3_phi + k4_phi);
        Phi_prim(i+1) = Phi_prim(i) + (h/6) * (k1_phi_prim + 2*k2_phi_prim + 2*k3_phi_prim + k4_phi_prim);
    end
end

% Iterativt minska steglängden h för att se till att
function [losning_halverad, fel, h] = iteration(method, g, m, L, my, h, t, phi0, phi_prim0, tolerans)
    fel = Inf; %Initiera fel som en stor siffra för att starta loopen
    while fel > tolerans %Medan fel större än tolerans upprepas 
        
        % Skapa tidsvektorn med aktuell steglängd h
        T = 0:h:t;
        % Beräkna lösning med aktuell steglängd h
        [~, losning, ~] = method(T, phi0, phi_prim0, h, m, my, g, L);
       
        % Skapa tidsvektorn med halverad steglängd h/2
        T_halverad = 0:h/2:t;
        % Beräkna lösning med halverad steglängd h/2
        [~, losning_halverad_full, ~] = method(T_halverad, phi0, phi_prim0, h/2, m, my, g, L);
        
        % Ta varannan punkt från lösningen med h/2 (för att jämföra med lösningen med h)
        losning_halverad = losning_halverad_full(1:2:end); % Ta varannan punkt i losning_halverad_full och placera den i losning_halverad
        diff = losning - losning_halverad;
        fel = norm(diff, inf); 
        h = h / 2;
    end
end