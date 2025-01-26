%Labb2 4a)
clear, clc 
fprintf('\n--------------------------------------- a) ----------------------------------------\n\n')

% Konstanter
m = 0.75;                        % Massa [kg]
x_plats = 20;                    % Målets x-position
g = 9.81;                        % Tyngdacceleration [m/s^2]
K = [0.004, 0; 0, 0.078];        % Luftmotståndsmatris [kg/m]
f = [0; -m * g];                 % Gravitationskraft [N]
v0 = 18.5;                       % Initial hastighet [m/s]
h0 = 0.5;                        % Initial höjd [m]
a = pi / 4;                      % Kastvinkel [rad]
tolerans = 1e-6;                 % Tolerans för nedslagsplats
h = 0.01;                        % Starttidsteg [s]
t_slut = 5;                      % Maximal tid för simulering [s]

% Initialvärden
x0 = 0;                          % Startposition x
y0 = h0;                         % Startposition y
v_x0 = v0 * cos(a);              % Initial hastighet i x-led
v_y0 = v0 * sin(a);              % Initial hastighet i y-led

% While-loop för att hitta tillräcklig precision
felaktighet = inf;               % Startvärde för felaktighet (stort initialvärde)
while felaktighet > tolerans
    % Skapa tidsvektor med aktuellt tidsteg
    t = 0:h:t_slut;

    % Beräkna kastbanan med aktuellt tidsteg
    [x, y, vx, vy] = varpkastbana(t, x0, y0, v_x0, v_y0, h, m, K, g);
    nedslagsplats = nedslagningsplats([x', y']); % Hitta var y = 0 (nedslag)

    % Beräkna kastbanan med dubbelt tidsteg för feluppskattning
    [x_2h, y_2h] = varpkastbana(t, x0, y0, v_x0, v_y0, h * 2, m, K, g);
    nedslagsplats_2h = nedslagningsplats([x_2h', y_2h']);

    % Uppdatera felaktigheten baserat på skillnad i nedslagsplatser
    felaktighet = norm(nedslagsplats_2h - nedslagsplats);

    % Halvera tidsteget för att öka noggrannheten
    h = h / 2; 
end

% Plotta den slutliga kastbanan
figure;
plot(x, y, 'm:', 'LineWidth', 2);                % Plotta x och y för kastbanan
xlabel('Marklängd');              % X-axel: marklängd
ylabel('Höjd');                   % Y-axel: höjd
hold on;
plot(nedslagsplats, 0, 'gx', 'MarkerSize', 16, 'LineWidth', 3); % Markera nedslagsplats
legend('Bana', 'Mål');
xlim([0, 25]);                    % Begränsa x-axelns visning
ylim([0, 6]);                     % Begränsa y-axelns visning
grid on;

% Skriv ut slutresultat
fprintf('Kastets nedslagsplats är: %.6f meter\n', nedslagsplats);
fprintf('Detta sker på det slutgiltiga tidsteget: h = %.4f\n', h*2);
fprintf('Felaktigheten med 6 antal korrekta decimaler uppskattas till: %.2e meter\n', felaktighet);



% --- Funktion för att hitta nedslagsplats ---
function nedslagsplats = nedslagningsplats(solution)
    % Extrahera x- och y-värden från lösningen
    x_varden = solution(:, 1);    % x-koordinater
    y_varden = solution(:, 2);    % y-koordinater

    % Leta efter var y-värdet ändrar tecken (korsar noll)
    for i = 2:length(y_varden)
        if y_varden(i) < 0        % Kontrollera när y blir negativ
            idx = i - 1;          % Spara index för sista positiva y-värdet
            break;
        end
    end

    % Välj punkter nära nollpassagen för interpolation
    x_nara_rot = x_varden(idx-1:idx+2);
    y_nara_rot = y_varden(idx-1:idx+2);

    % Anpassa ett kubiskt polynom till dessa punkter
    koefficienter = polyfit(x_nara_rot, y_nara_rot, 3);

    % Hitta rötterna till polynomet
    nollpunkt = roots(koefficienter);

    % Filtrera fram den giltiga roten inom intervallet
    nedslagsplats = nollpunkt(imag(nollpunkt) == 0 & ...
                              nollpunkt >= min(x_nara_rot) & ...
                              nollpunkt <= max(x_nara_rot));
    nedslagsplats = nedslagsplats(1); % Returnera den första giltiga roten
end

% --- Funktion för att beräkna kastbana med Runge-Kutta 4 ---
function [x, y, vx, vy] = varpkastbana(t, x0, y0, v_x0, v_y0, h, m, K, g)
    n = length(t);                % Antal tidssteg
    x = zeros(1, n);              % Initiera x-vektor
    y = zeros(1, n);              % Initiera y-vektor
    vx = zeros(1, n);             % Initiera vx-vektor
    vy = zeros(1, n);             % Initiera vy-vektor

    % Startvärden
    x(1) = x0;                    
    y(1) = y0;
    vx(1) = v_x0;
    vy(1) = v_y0;

    % Runge-Kutta 4-metoden för att lösa differentialekvationer
    for i = 1:n-1
        % Steg 1
        k1_x = vx(i);
        k1_y = vy(i);        
        k1_vx = -K(1,1)/m * k1_x * sqrt(vx(i)^2 + vy(i)^2);   
        k1_vy = -g - K(2,2)/m * k1_y * sqrt(vx(i)^2 + vy(i)^2);
        
        % Steg 2
        k2_x = vx(i) + h * k1_vx/2;
        k2_y = vy(i) + h * k1_vy/2;
        k2_vx = -K(1,1)/m * k2_x * sqrt(k2_x^2 + k2_y^2);
        k2_vy = -g - K(2,2)/m * k2_y * sqrt(k2_x^2 + k2_y^2);
        
        % Steg 3
        k3_x = vx(i) + h * k2_vx/2;
        k3_y = vy(i) + h * k2_vy/2;
        k3_vx = -K(1,1)/m * k3_x * sqrt(k3_x^2 + k3_y^2);
        k3_vy = -g - K(2,2)/m * k3_y * sqrt(k3_x^2 + k3_y^2);
        
        % Steg 4
        k4_x = vx(i) + h * k3_vx;
        k4_y = vy(i) + h * k3_vy;
        k4_vx = -K(1,1)/m * k4_x * sqrt(k4_x^2 + k4_y^2);
        k4_vy = -g - K(2,2)/m * k4_y * sqrt(k4_x^2 + k4_y^2);
        
        % Uppdatera värdena för nästa tidssteg
        x(i+1) = x(i) + (h/6) * (k1_x + 2*k2_x + 2*k3_x + k4_x);
        y(i+1) = y(i) + (h/6) * (k1_y + 2*k2_y + 2*k3_y + k4_y);
        vx(i+1) = vx(i) + (h/6) * (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx);
        vy(i+1) = vy(i) + (h/6) * (k1_vy + 2*k2_vy + 2*k3_vy + k4_vy);
    end
end


%% Labb2 4b)
fprintf('\n--------------------------------------- b) ----------------------------------------\n')

% Startgissningar för kastvinkeln alpha
a_lag = 0.01;                  % Låg gissning nära 0 radianer (nära horisontellt kast)
a_hog = (pi / 2) - 0.01;       % Hög gissning nära 90 grader (nära lodrätt kast)

% Hitta optimal kastvinkel för låg och hög bana med hjälp av bisektionsmetoden
[optimala_a_lag, lag_nedslagsplats] = gynnsammast_vinkel(t, h, tolerans, [a_lag, a], x0, y0, v0, m, K, g, x_plats);
[optimala_a_hog, hog_nedslagsplats] = gynnsammast_vinkel(t, h, tolerans, [a, a_hog], x0, y0, v0, m, K, g, x_plats);

% Tidsvektor för att simulera kastbanor
t_slut = 5;
t = 0:h:t_slut;

% Beräkna kastbanor för de optimala vinklarna
[x_lag, y_lag] = varpkastbana(t, 0, h0, v0 * cos(optimala_a_lag), v0 * sin(optimala_a_lag), h, m, K, g);
[x_hog, y_hog] = varpkastbana(t, 0, h0, v0 * cos(optimala_a_hog), v0 * sin(optimala_a_hog), h, m, K, g);

% Plotta de optimala kastbanorna
figure;
plot(x_lag, y_lag, 'k--', 'LineWidth', 1.5); % Låg bana
hold on;
plot(x_hog, y_hog, 'm:', 'LineWidth', 1.5); % Hög bana
plot(x_plats, 0, 'gx', 'MarkerSize', 16, 'LineWidth', 3); % Målet
xlabel('x-position (m)');
ylabel('y-position (m)');
title('Optimala kastbanor');
legend('Låg bana', 'Hög bana', 'Mål');
grid on;
xlim([0, 25]); % Begränsa x-axeln
ylim([0, 6]);  % Begränsa y-axeln

% Skriv ut resultaten i kommandofönstret
fprintf('\nLåg banas gynnsammaste kastvinkel: %.6f rad\n', optimala_a_lag);
fprintf('Hög banas gynnsammaste kastvinkel: %.6f rad\n', optimala_a_hog);
fprintf('\nLåg banas nedslagsplats: %.6f meter\n', lag_nedslagsplats);
fprintf('Hög banas nedslagsplats: %.6f meter\n', hog_nedslagsplats);



% --- Funktion för att hitta den optimala kastvinkeln ---
function [a_gynn, x_landing] = gynnsammast_vinkel(t, h, tolerans, a_gissning, x0, y0, v0, m, K, g, x_malsattning)
    % a_gynn: Optimal kastvinkel
    % x_landing: Nedslagsplatsen för den optimala kastvinkeln
    % a_gissning: Intervall för vinklar [a1, a2]
    
    % Extrahera gränser från gissningsintervallet
    a1 = a_gissning(1); % Lägre gräns för vinkeln
    a2 = a_gissning(2); % Övre gräns för vinkeln
    max_iter = 100;     % Max antal iterationer för bisektionsmetoden
    curriter = 0;       % Håller reda på antalet iterationer

    % Starta bisektionsmetoden för att hitta optimal vinkel
    while abs(a2 - a1) > tolerans && curriter < max_iter
        % Beräkna mittenvinkeln
        a_mitten = (a1 + a2) / 2;

        % Beräkna nedslagsplats för mittenvinkeln
        vx_mid = v0 * cos(a_mitten);
        vy_mid = v0 * sin(a_mitten);
        [x_mid, y_mid] = varpkastbana(t, x0, y0, vx_mid, vy_mid, h, m, K, g);
        x_mittenlandning = nedslagningsplats([x_mid', y_mid']);

        % Beräkna avvikelsen från målet
        F_mitten = x_mittenlandning - x_malsattning;

        % Beräkna nedslagsplats för den lägre gränsen
        vx_1 = v0 * cos(a1);
        vy_1 = v0 * sin(a1);
        [x1, y1] = varpkastbana(t, x0, y0, vx_1, vy_1, h, m, K, g);
        x_landing1 = nedslagningsplats([x1', y1']);
        F1 = x_landing1 - x_malsattning;

        % Uppdatera gränserna baserat på bisektionsmetoden
        if F1 * F_mitten < 0
            a2 = a_mitten; % Justera övre gränsen
        else
            a1 = a_mitten; % Justera nedre gränsen
        end

        curriter = curriter + 1; % Öka iterationen
    end

    % Returnera optimal vinkel och slutlig nedslagsplats
    a_gynn = (a1 + a2) / 2; % Optimal kastvinkel
    vx_gynn = v0 * cos(a_gynn); % Hastighet i x-led vid optimal vinkel
    vy_gynn = v0 * sin(a_gynn); % Hastighet i y-led vid optimal vinkel
    [x_final, y_final] = varpkastbana(t, x0, y0, vx_gynn, vy_gynn, h, m, K, g);
    x_landing = nedslagningsplats([x_final', y_final']); % Slutlig nedslagsplats
end


%% Uppgift c)
fprintf('\n--------------------------------------- c) ----------------------------------------\n')

% Skapa störda startvinklar och hastigheter
a_andra_lag = optimala_a_lag * [0.95, 1.05]; % Variationer av låg bana: ±5% av optimal vinkel
v0_andra_lag = v0 * [0.95, 1.05];            % Variationer av hastighet: ±5% av initialhastighet
a_andra_hog = optimala_a_hog * [0.95, 1.05]; % Variationer av hög bana: ±5% av optimal vinkel
v0_andra_hog = v0 * [0.95, 1.05];            % Variationer av hastighet: ±5% av initialhastighet

% Initiera vektorer för att lagra nedslagsplatser
x_landings_lag = zeros(4, 1); % Nedslagsplatser för låg bana
x_landings_hog = zeros(4, 1); % Nedslagsplatser för hög bana

% --- Simulera störda kast för låg bana ---
for i = 1:2 % Iterera över de två störda vinklarna
    % Beräkna initiala hastigheter i x- och y-led för varje störd vinkel
    v_x0_lag_i = v0_andra_lag .* cos(a_andra_lag(i));
    v_y0_lag_i = v0_andra_lag .* sin(a_andra_lag(i));
    for j = 1:2 % Iterera över de två störda hastigheterna
        % Simulera kastbanan för varje kombination av vinkel och hastighet
        [x_lag, y_lag] = varpkastbana(t, x0, y0, v_x0_lag_i(j), v_y0_lag_i(j), h, m, K, g);

        % Beräkna och lagra nedslagsplatsen
        x_landings_lag(2 * (i - 1) + j) = nedslagningsplats([x_lag', y_lag']);
    end
end

% --- Simulera störda kast för hög bana ---
for i = 1:2 % Iterera över de två störda vinklarna
    % Beräkna initiala hastigheter i x- och y-led för varje störd vinkel
    v_x0_hog_i = v0_andra_hog .* cos(a_andra_hog(i));
    v_y0_hog_i = v0_andra_hog .* sin(a_andra_hog(i));
    for j = 1:2 % Iterera över de två störda hastigheterna
        % Simulera kastbanan för varje kombination av vinkel och hastighet
        [x_hog, y_hog] = varpkastbana(t, x0, y0, v_x0_hog_i(j), v_y0_hog_i(j), h, m, K, g);

        % Beräkna och lagra nedslagsplatsen
        x_landings_hog(2 * (i - 1) + j) = nedslagningsplats([x_hog', y_hog']);
    end
end

% --- Beräkna maximal avvikelse från målet ---
avvikelse_lag = max(abs(x_landings_lag - x_plats)); % Maximal avvikelse för låg bana
avvikelse_hog = max(abs(x_landings_hog - x_plats)); % Maximal avvikelse för hög bana

% --- Skriv ut resultaten ---
fprintf('\nDen största avvikelsen för låg bana: %.3f meter\n', avvikelse_lag);
fprintf('Den största avvikelsen för hög bana: %.3f meter\n', avvikelse_hog);