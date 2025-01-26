%% uppgift 4a)
clc, clear

load ('dollarkurs.mat');
t=day;
x=USDSEK;

%Kom ihåg att g=c0+c1*t
A = [ones(length(t), 1), t]; % Matris med en kolumn av ettor och tidsdata, detta är vad c multipliceras med, c*1 och c*tidsdatan (t)
%A*c=x; 
c=A\x; %Detta ser till att vi får fram värdet på c
g=A*c;

figure;
plot(t, x, 'b.', 'DisplayName', 'Dollarkursdata'); % Plotta den faktiska dollarkursen, t är x-axeln (dagarna), x är y-axeln (dollarkursen i SEK), b=blå, 
hold on; %Får den att stanna kvar så nästa kan placeras ovanpå
plot(t, g, 'r', 'DisplayName', 'Anpassad Linjär Modell'); % Plotta den linjära anpassningen, t är x-axeln (dagarna), g är y-axeln (anpassade linjära modellen), r=röd
xlabel('Dag');
ylabel('Dollarkurs i SEK');
title('Anpassning av Dollarkursdata med Linjär Modell');
legend; %Detta är den lilla rektangeln i bilden
grid on;

% Skriv ut värdena på koefficienterna
fprintf('Koefficienter:\n c0 = %.4f, c1 = %.4f\n', c(1), c(2));

% Beräkna medelkvadratfelet
N = length(t);
medelkvadratfel = sum((x - g).^2) / N;
fprintf('\nMedelkvadratfelet: %.4f\n', medelkvadratfel);


%% uppgift 4b)

load ("dollarkurs.mat")
t=day;
x1=USDSEK;
L=980;

%g2=d0 + d1*t + d2*sin(2*pi*t/L) + d3*cos(2*pi*t/L);
% Felberäkning:
listan_av_fel = []; %En lista för alla felen
for i = 1:length(t)
    fel = x(i) - g(i);  % Beräkna felet för varje punkt
    listan_av_fel(i) = fel; 
end

figure;
plot(t, listan_av_fel, 'm');
xlabel('Index för datapunkt');
ylabel('Felaktig');
title('Felaktigheter mellan data och den linjära modellen');
grid on

%Lösa ekvationen
A=[ones(length(t), 1), t, sin(2*pi*t/L), cos(2*pi*t/L)];
%A*d=x
d=A\x1;
g2=A*d;

figure;
plot(t, x1, 'b.', 'DisplayName', 'Dollarkursdata'); % Plotta den faktiska dollarkursen, t är x-axeln (dagarna), x är y-axeln (dollarkursen i SEK), b=blå, 
hold on; %Får den att stanna kvar så nästa kan placeras ovanpå
plot(t, g2, 'k', 'DisplayName', 'Anpassad modell mha Cosinus och Sinus')
xlabel('Dag')
ylabel('Dollarkurs i SEK')
title ('Anpassning av Dollarkursdata mha Cosinus och Sinus')
legend;
grid on;

fprintf('\nKoefficienterna:\n d0=%.4f\n d1=%.4f\n d2=%.4f\n d3=%.4f\n', d(1), d(2), d(3), d(4));

%Medelkvadratfel
N1=length(t);
medelkvadratfel = sum((x1-g2).^2)/N1;
fprintf('\nMedelkvadratfel: %.4f\n', medelkvadratfel)


%% uppgift 4c)
%Gauss-Newton metoden är en optimeringsmetod som används för att lösa icke-linjära minstakvadratproblem 
% och en variant av Newtons metod som är specifikt utformad för att passa situationer där man vill minimera 
% summan av kvadraterna för fel mellan observerade data och en modell. 

% Ladda in data
load("dollarkurs.mat");

t = day;        % Tidsvektorn (dagar)
x2 = USDSEK;    % Dollarkursen

% Startgissning baserad på resultatet från b)
d0=8.5540;
d1=0.0012;
d2=0.2650;
d3=0.8376;
L=980;        

% Samla initiala gissningar i en vektor
K = [d0; d1; d2; d3; L];
% Tolerans och max antal iterationer
tolerans = 1e-6;
maxiter = 100;

% Gauss-Newton iteration
for iter = 1:maxiter
    % Beräkna modellen
    g3 = K(1) + K(2) * t + K(3) * sin(2 * pi * t / K(5)) + K(4) * cos(2 * pi * t / K(5));

    % Felvärde
    felvarden = x2 - g3;
    % Beräkna Jacobianen
    J = [ones(length(t), 1), t, sin(2 * pi * t / K(5)), cos(2 * pi * t / K(5)), (K(3) * (-2 * pi * t / K(5)^2) .* cos(2 * pi * t / K(5))) + (K(4) * (2 * pi * t / K(5)^2) .* sin(2 * pi * t / K(5)))];
    % Uppdatera parametrarna med Gauss-Newton-formeln: Formeln är:
    % (TransponatJ * J)^-1/(TransponatJ*felvarden) = (TransponatJ*J)\(Transponat*felvarden)
    delta_K = (J' * J) \ (J' * felvarden);
    K = K + delta_K; %Nu får vi alltså de K som är de ULTIMATA värdena på d0, d1, d2, d3, L, genom Gauss-Newton som vi gjrode innan blir värdena nu helt optimala.
    
    % Kontrollera konvergens, om 
    if norm(delta_K) < tolerans
        break;
    end
end

% Skriv ut de optimerade parametrarna
fprintf('Optimerade parametrar:\n d0 = %.4f\n d1 = %.4f\n d2 = %.4f\n d3 = %.4f\n L = %.4f\n', K(1), K(2), K(3), K(4), K(5));
% Beräkna den anpassade modellen med de optimerade parametrarna
g3 = K(1) + K(2) * t + K(3) * sin(2 * pi * t / K(5)) + K(4) * cos(2 * pi * t / K(5));

% Plotta den faktiska dollarkursen och den anpassade modellen
figure;
plot(t, x2, 'b.', 'DisplayName', 'Dollarkursdata');
hold on;
plot(t, g3, 'm', 'DisplayName', 'Anpassad modell med Gauss-Newton');
xlabel('Dag');
ylabel('Dollarkurs i SEK');
title('Anpassning av Dollarkursdata med Gauss-Newton och Justerbar Period');
legend;
grid on;

% Beräkna och skriv ut medelkvadratfelet
N2 = length(t);
medelkvadratfel = sum((x2 - g3).^2) / N2;
fprintf('\nMedelkvadratfel: %.4f\n', medelkvadratfel);

%plot alla modeller i samma figur
figure;
plot(t, x, 'b.', 'DisplayName', 'Dollarkursdata');  % Faktisk dollarkursdata
hold on;
plot(t, g, 'r', 'DisplayName', 'Linjär modell');  % Linjär modell, första
plot(t, g2, 'k', 'DisplayName', 'Sinus och Cosinus modell');  % Sinus och cosinusmodell, andra
plot(t, g3, 'm', 'DisplayName', 'Gauss-Newton optimerad modell');  % Gauss-Newton-modell, tredje