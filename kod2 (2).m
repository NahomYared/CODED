%% uppgift 2a) Lösning skickas i en annan fil


%% uppgift 2b) 
clc, clear

% Definiera som vektorer
koordinater_av_a = [-1.5, 3.0]; % [a_x, a_y]
koordinater_av_b = [1.0, 1.0]; % [b_x, b_y]
radier = [1.5, 0.8]; % [r_a, r_b]
maximal_iteration = 1000; %Maximala antalet iterationer
tolerans = 1e-11; %Toleransnivå för konvergensen

% newtons metod anropas
[x1, antal_iterationer] = newtons_metod(@Jacobimatris, @F, tolerans, maximal_iteration, koordinater_av_a, koordinater_av_b, radier, 1);
% Funktionen newtons_metod definieras här, löser ekvsystemet mha Newtons metod och använder parametrarna från Jacobimatrisacobimatris, F, tolerans, maximal_iteration,
% Koordinater av a och b och radierna.  [x, antal_iterationer] = Utdata!!
function [x, antal_iterationer] = newtons_metod(Jacobimatris, F, tolerans, maximal_iteration, koordinater_av_a, koordinater_av_b, radier, i)
    
    %Definition av vad de olika värdena är.
    x_a = koordinater_av_a(1); 
    y_a = koordinater_av_a(2);
    x_b = koordinater_av_b(1);
    y_b = koordinater_av_b(2);
    r_a = radier(1);
    r_b = radier(2);
    
    felvarde = tolerans + 1; %Den görs till  +1 för att garantera att felvärde är högre än toleransen, annars kommer ingenting att run.
    antal_iterationer = 0; %Initiera antalet iterationer till noll
    
    %x0 är startgissningen, baserat på i så fås ett annorlunda x0. x0 ska
    %representera olika koordinater på vart den kan vara någonstans för
    %bästa. Alltså om i är lika med 1 så är x0=[-1.5+1.5, 3+1.5, 1+0.8, 1+0.8]=[0, 4.5, 1.8, 1.8]
    
    if i == 1
        x0 = [x_a + r_a, y_a + r_a, x_b + r_b, y_b + r_b]';
    elseif i == 2
        x0 = [x_a - r_a, y_a + r_a, x_b - r_b, y_b + r_b]';
    elseif i == 3
        x0 = [x_a + r_a, y_a - r_a, x_b + r_b, y_b - r_b]';
    else
        x0 = [x_a - r_a, y_a - r_a, x_b - r_b, y_b]';
    end
    
    %Iterera tills felvärde är mindre än tolerans eller max antal iterationer nås
    while (felvarde > tolerans) && (antal_iterationer < maximal_iteration)
        %Jacobimatris_1 fås genom funktionen Jacobimatris
        Jacobimatris_1 = Jacobimatris(x0(1), x0(2), x0(3), x0(4), x_a, y_a, x_b, y_b); %Man de 4 värdena från x0 och sedan koordinaterna för mittpunkerna av cirklarna och stoppar in de som parametrar i funktionen
        %Man de 4 värdena från x0 och sedan koordinaterna för mittpunkerna av cirklarna och radierna för att få fram funktionen F
        F1 = F(x0(1), x0(2), x0(3), x0(4), x_a, y_a, x_b, y_b, r_a, r_b);
       
        %Newtons metod för icke-linjära system, såsom cirklar: x=x0 - Jacobimatris_1^-1/F1, alltså:
        x = x0 - (Jacobimatris_1 \ F1); %Detta behövs dock senare inte till 2c)
        % Beräkna felet mellan den nya och den gamla gissningen (norm av skillnaden). Anledningen till att vi använder normen av skillnaden mellan den nya och den gamla gissningen i Newtons metod är för att mäta hur my_cket gissningen förändras mellan iterationerna. Detta hjälper oss att avgöra om vi har kommit tillräckligt nära en lösning.
        felvarde = norm(x - x0);
        %Uppdatera gissnignen till nästa funktion
        x0 = x;
        antal_iterationer = antal_iterationer + 1;
    end
end

% Funktion som berättar vad vi fick i a) på värden värdena av F1, F2, F3,
% F4. Detta skrevs på papper. Funktion för F1 (avståndet mellan cirkel A och punkt (x1,y1))
function f1 = F1(x1, y1, x_a, y_a, r_a)
    f1 = (x1 - x_a)^2 + (y1 - y_a)^2 - r_a^2;
end
% Funktion för F2 (avståndet mellan cirkel B och punkt (x2,y2))
function f2 = F2(x2, y2, x_b, y_b, r_b)
    f2 = (x2 - x_b)^2 + (y2 - y_b)^2 - r_b^2;
end
% Funktion för F3 (tangentvillkor mellan punkt (x1,y1) och (x2,y2) på cirklarna)
function f3 = F3(x1, y1, x2, y2, x_a, y_a)
    f3 = (x1 - x2) * (x1 - x_a) + (y1 - y2) * (y1 - y_a);
end
% Funktion för F4 (tangentvillkor mellan punkt(x1,y1) och (x2,y2) på cirklarna)
function f4 = F4(x1, y1, x2, y2, x_b, y_b)
    f4 = (x1 - x2) * (x2 - x_b) + (y1 - y2) * (y2 - y_b);
end
% Huvudfunktion som kombinerar alla F-komponenter
function F_result = F(x1, y1, x2, y2, x_a, y_a, x_b, y_b, r_a, r_b)
    F_result = [F1(x1, y1, x_a, y_a, r_a);
                F2(x2, y2, x_b, y_b, r_b);
                F3(x1, y1, x2, y2, x_a, y_a);
                F4(x1, y1, x2, y2, x_b, y_b)];
end
% Funktion av Jacobimatris, det är derivatorna av F1,F2,F3,F4 och de är
% skrivna som [dF1/dx1, dF1/dy1, dF1/dx2, dF1/dy2, och samma för F2. Detta
% gjordes också på papper i fråga a)
function resultat = Jacobimatris(x1, y1, x2, y2, x_a, y_a, x_b, y_b)
    resultat = [2 * (x1 - x_a), 2 * (y1 - y_a), 0, 0;
                0, 0, 2 * (x2 - x_b), 2 * (y2 - y_b);
                2 * x1 - x2 - x_a, 2 * y1 - y_a - y2, x_a - x1, y_a - y1;
                x2 - x_b, y2 - y_b, -2 * x2 + x1 + x_b, -2 * y2 + y1 + y_b];
end

hold on; %Utan denna kommer endast linjen synas, denna funktion ser till att linjen hålls kvar i bilden tills senare när cirklarna ska ritas
rita_linjen_och_cirklar(x1, koordinater_av_a, koordinater_av_b, radier);%Funktion för att rita linjen mellan cirklarna
hold off;
fprintf("Antal iterationer: %.d, (x1, y1), (x2, y2) = (%.10f, %.10f), (%.10f, %.10f) \n", antal_iterationer, x1(1), x1(2), x1(3), x1(4));

% Funktion för att rita en cirkel, 
function rita_cirkel(x_c, y_c, radie, farg)
    theta = linspace(0, 2 * pi, 100); %Från 0 till 2pi med 100 punkter
    x = radie * cos(theta) + x_c;
    y = radie * sin(theta) + y_c;
    plot(x, y, 'Color', farg, 'LineWidth', 1.5);
end

% Funktion för att rita linjen mellan punkter på två cirklar
function rita_linjen_och_cirklar(x, koordinater_av_a, koordinater_av_b, radier)
    % Rita cirklarna först
    rita_cirkel(koordinater_av_a(1), koordinater_av_a(2), radier(1), 'k');
    rita_cirkel(koordinater_av_b(1), koordinater_av_b(2), radier(2), 'm');
    %Mittpunkterna i cirklarna
    rita_cirkel(koordinater_av_a(1), koordinater_av_a(2), 0.02, 'k');
    rita_cirkel(koordinater_av_b(1), koordinater_av_b(2), 0.02, 'm');
    % Rita linjen mellan punkterna
    plot([x(1), x(3)], [x(2), x(4)], '-*', 'LineWidth', 2, 'MarkerSize', 8);
    xlabel('x');
    ylabel('y');
    axis equal;
end

% Funktion: langd
% Denna funktion beräknar den totala längden av snöret genom att summera längden mellan varje del (linjär och cirkelsektor). Denna används i c)
function langd = langd(tolerans, maximal_iteration, koordinater_av_a, koordinater_av_b, koordinater_av_c, radier_ab, radier_bc, radier_ca)
    [x2, ~] = newtons_metod(@Jacobimatris, @F, tolerans, maximal_iteration, koordinater_av_a, koordinater_av_b, radier_ab, 2); %~ används när man vill ignorera en utdata från en funktion.
    [x3, ~] = newtons_metod(@Jacobimatris, @F, tolerans, maximal_iteration, koordinater_av_b, koordinater_av_c, radier_bc, 3);
    [x4, ~] = newtons_metod(@Jacobimatris, @F, tolerans, maximal_iteration, koordinater_av_c, koordinater_av_a, radier_ca, 4);
    
    langd1 = norm([x2(1), x2(2)]-[x2(3), x2(4)]) + norm([x3(1), x3(2)]-[x3(3), x3(4)]) + norm([x4(1), x4(2)]-[x4(3), x4(4)]);
    langd2 = cirkelsektor(x2, x3, radier_ab(2)) + cirkelsektor(x3, x4, radier_ca(1)) + cirkelsektor(x4, x2, radier_ca(2));
    langd = langd1 + langd2;
end

% Funktion: cirkelsektor
% Denna funktion beräknar längden av en cirkelsektor mellan två punkter på cirkeln med given radie
function langd = cirkelsektor(x1, x2, r)
    % Beräkna vinkeln mellan punkterna på cirkeln, asin=arcsin
    phi = 2 * asin((1 / 2) * (norm([x1(3), x1(4)] - [x2(1), x2(2)]) / r));
    % Längden av sektorn är radien multiplicerad med vinkeln
    langd = phi * r;
end



%% uppgift 2c) 
clc, clear

% Inställningar
tolerans = 1e-11; % Tolerans för konvergens
maximal_iteration = 1000; % Maximalt antal iterationer

% Definiera koordinater och radier som separata skalära värden
koordinater_av_a = [-1.0, 1.5];
koordinater_av_b = [3.0, 0.5];
koordinater_av_c = [0.0, -2.0];
radier_ab = [1.0, 1.2]; % Radier mellan A och B
radier_bc = [1.2, 1.7]; % Radier mellan B och C
radier_ca = [1.7, 1.0]; % Radier mellan C och A

% Anropa Newtons metod för varje segment mellan cirklarna, mellan C-A, B-C
% och A-B
[x2, ~] = newtons_metod(@Jacobimatris, @F, tolerans, maximal_iteration, koordinater_av_a, koordinater_av_b, radier_ab, 2);
[x3, ~] = newtons_metod(@Jacobimatris, @F, tolerans, maximal_iteration, koordinater_av_b, koordinater_av_c, radier_bc, 3);
[x4, ~] = newtons_metod(@Jacobimatris, @F, tolerans, maximal_iteration, koordinater_av_c, koordinater_av_a, radier_ca, 4);

% Beräkna totala längden på snöret
totala_langden = langd(tolerans, maximal_iteration, koordinater_av_a, koordinater_av_b, koordinater_av_c, radier_ab, radier_bc, radier_ca);
fprintf("Längden på snöret är: %.5f längdenheter \n", totala_langden);

% Plotta hela slingan
figure;
hold on;
% Använd de redan definierade funktionerna för att rita cirklarna och linjen. Genom att lägga till dessa argumenten ritas de nya cirklarna
rita_linjen_och_cirklar(x2, koordinater_av_a, koordinater_av_b, radier_ab);
rita_linjen_och_cirklar(x3, koordinater_av_b, koordinater_av_c, radier_bc);
rita_linjen_och_cirklar(x4, koordinater_av_c, koordinater_av_a, radier_ca);
grid on;
hold off;



%% uppgift 2d) 

% Globala variabler 
E = 0.01; % Definiera storleken på storningen
tolerans = 1e-11;
maximal_iteration = 1000;

[E_tot, lista_storning] = storning(tolerans, maximal_iteration, koordinater_av_a, koordinater_av_b, koordinater_av_c, radier_ab, radier_bc, radier_ca, E);
[varde, index] = max(lista_storning);
fprintf('storningsanalys ger att längden är: %.4f (+/-) %.4f \n', totala_langden, E_tot);
fprintf('Index %d ger största felet, bidrar med: (+/-) %.4f \n', index, varde);

% Funktion: storning
% Funktionen beräknar hur längden påverkas av små storningar på olika parametrar (koordinater och radier)
function [E_tot, lista_storning] = storning(tolerans, maximal_iteration, koordinater_av_a, koordinater_av_b, koordinater_av_c, radier_ab, radier_bc, radier_ca, E)
   
% Skapa en vektor som innehåller alla parametrar som vi vill störa.
    parameter_vektor = [koordinater_av_a, koordinater_av_b, koordinater_av_c, radier_ab, radier_bc, radier_ca];
    
    % Initiera en lista som kommer att hålla storningsvärdena
    lista_storning = zeros(1, length(parameter_vektor)); %en rad och kolumner lika många som parameter_vektors längd med endast nollor.
    
    % Beräkna den ursprungliga längden utan storning 
    originell_langd = langd(tolerans, maximal_iteration, koordinater_av_a, koordinater_av_b, koordinater_av_c, radier_ab, radier_bc, radier_ca);
    
    % Iterera över alla parametrar och applicera en storning E på varje parameter
    for i = 1:length(parameter_vektor)
        % Kopiera parametrarna och applicera storning på den i:te parametern
        parameter_vektor_storning = parameter_vektor;
        parameter_vektor_storning(i) = parameter_vektor_storning(i) + E;
        
        % Dela upp de störda parametrarna i rätt variabler (koordinater och radier)
        koordinater_av_a_storning = parameter_vektor_storning(1:2);  % Störda koordinater för A
        koordinater_av_b_storning = parameter_vektor_storning(3:4);  % Störda koordinater för B
        koordinater_av_c_storning = parameter_vektor_storning(5:6);  % Störda koordinater för C
        radier_ab_storning = parameter_vektor_storning(7:8);  % Störda radier för AB
        radier_bc_storning = parameter_vektor_storning(9:10);  % Störda radier för BC
        radier_ca_storning = parameter_vektor_storning(11:12);  % Störda radier för CA
        
        % Beräkna längden på snöret med de störda parametrarna
        langd_storning = langd(tolerans, maximal_iteration, koordinater_av_a_storning, koordinater_av_b_storning, koordinater_av_c_storning, radier_ab_storning, radier_bc_storning, radier_ca_storning);
        
        % Beräkna skillnaden (storningen) mellan den ursprungliga längden och den störda längden
        lista_storning(i) = abs(originell_langd - langd_storning); % Använder absolutvärde för att undvika negativa storningsvärden
    end
    
    % Summera alla storningar för att få den totala påverkan (totala_E)
    E_tot = sum(lista_storning);
end


% Index 10 är rc, radien av c