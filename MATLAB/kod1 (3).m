%% uppgift 1a)
clc, clear

% 1a)
% Här letar vi efter ett lämpligt startvärde för nollställen genom att plotta 
% den givna funktionen y1 inom intervallet [0, 10]. Detta ger en grafisk representation
% av var funktionens nollställen kan finnas.

y1 = @(x) x.^2-8*x-12*sin(3*x+1)+19; % Definierar funktionen y1
fplot(y1, [0,10]) % Plottar y1 för att undersöka var nollställen kan ligga
hold
grid on
plot(xlim,[0,0]) % Lägg till en horisontell linje vid y = 0
xlabel x 
ylabel y 


%% uppgift 1b) och c)
clc, clear

% Definiera startgissningarna
xv = [1.97, 2.66, 3.94, 4.81, 6.16, 6.64];

% Definiera funktionen f(x) och dess derivata
y1 = @(x) x.^2 - 8*x - 12*sin(3*x + 1) + 19;
dy1 = @(x) 2*x - 36*cos(3*x + 1) - 8;

% Definiera fixpunktfunktionen phi(x)
phi = @(x) (1/19) * (x.^2 + 11*x - 12*sin(3*x + 1)) + 1;
dphi = @(x) (1/19) * (2*x + 11 - 36*cos(3*x + 1));

% Globala parametrar
tolerans = 1e-10;
maxiter = 1000;

% Kör funktionerna för varje startgissning
for i = 1:length(xv)
    x0 = xv(i); % Startgissning för varje i (1-6)
    
    % Kontrollera derivatans värde för fixpunktfunktionen vid startgissningen
    if abs(dphi(x0)) < 1
        % Använd fixpunktiteration
        fprintf('\nAnvänder fixpunktiteration för startgissning: %.2f\n', x0);
        [xf, niterf, ~] = fixpoint(phi, x0, tolerans, maxiter);
        fprintf('Fixpunktapproximation: %.10f, Iterationer: %d\n', xf, niterf);
    else
        % Avbryt fixpunktiteration och meddela att konvergens saknas
        fprintf('\nIngen konvergens för fixpunktiteration med startgissning %.2f (|phi''(x)| > 1)\n', x0);
    end
    
    % Använd Newtons metod
    fprintf('\nAnvänder Newtons metod för startgissning %.2f\n', x0);
    [xn, nitern, ~] = newton(y1, dy1, x0, tolerans, maxiter, false);
    fprintf('Newtonapproximation: %.10f, Iterationer: %d\n', xn, nitern);
end

% Funktion för Newtons metod
function [x, niter, xlista] = newton(y, dy, x0, tolerans, maxiter, uppgd)
    g = @(x) x - y(x) / dy(x);
    [x, niter, xlista] = fixpoint(g, x0, tolerans, maxiter);
    if uppgd
        fprintf('Bästa x-approximationen: x = %.15f\n', x);
    end
end

% Funktion för fixpunktiteration
function [x, niter, xlista] = fixpoint(phi, x0, tolerans, maxiter)
    x = x0;
    xlista = x0;
    niter = 0;
    res = tolerans + 1;
    
    while (res > tolerans) && (niter < maxiter)
        x_new = phi(x);
        res = abs(x_new - x);
        x = x_new;
        
        % Spara nuvarande värde
        xlista = [xlista, x];
        niter = niter + 1;
    end
end


%% uppgift 1d)
clear,clc

% Funktioner och metoder för att jämföra Newtons och sekantmetoden
y1 = @(x) x.^2-8*x-12*sin(3*x+1)+19; 
dy1 = @(x) 2*x - 36*cos(3*x + 1) - 8; 
phi = @(x) (x.^2+11*x-12*sin(3*x+1))/19+1; 
x0 = 6.64; % Startvärde nära ett nollställe

% Definierar felgränser och max antal iterationer
tolerans = 1e-15;
tolerans2 = 1e-10;
maxiter = 1000;

uppgd = true; % Sätter flagga för att skriva ut resultat

% Använder Newtons metod för att få referenslösning
[x_referens, antal_iterationer, iter_lista] = newton(y1, dy1, x0, tolerans, maxiter, false);
fprintf('Referenslösning x* = %.15f\n', x_referens);

% Deluppgift i) Beräknar lösningar med både sekantmetoden och Newtons metod
[varde_sekant, iterationer_sekant,iter_lista_sekant] = fixpoint(phi, x0, tolerans2, maxiter); % Fixpunktsmetod
[varde_newton, iterationer_newton,iter_lista_newton] = newton(y1,dy1,x0, maxiter,tolerans2, false); % Newtonmetod

% Deluppgift i) Beräknar fel i varje iteration relativt referenslösningen
for i = 1:length(iter_lista_sekant)
    fel_sekant = norm(iter_lista_sekant(i) - x_referens); % Fel för fixpointmetoden
    fel_sekant_lista(i) = fel_sekant;
end

for i = 1:length(iter_lista_newton)
    fel_newton = norm(iter_lista_newton(i) - x_referens); % Fel för Newtons metod
    fel_newton_lista(i) = fel_newton;
end

% Plottar felkonvergens för båda metoderna
figure('Name','Felkonvergens för båda metoderna','NumberTitle','off');
semilogy(1:length(fel_sekant_lista), fel_sekant_lista,'m') % Sekantmetoden i magenta
hold on
semilogy(1:length(fel_newton_lista),fel_newton_lista,'r') % Newtons metod i rött

% Deluppgift ii) Beräknar ordningen av konvergens för båda metoderna
for i = 1:(length(fel_sekant_lista)-1)
    fel_sekant_lista_iter(i) = fel_sekant_lista(i+1); % Sekantfel för nästa iteration
end 

for i = 1:(length(fel_newton_lista)-1)
    fel_newton_lista_iter(i) = fel_newton_lista(i+1); % Newtonfel för nästa iteration
end

% Plottar konvergensordningen för båda metoderna
figure('Name','Konvergensordning','NumberTitle','off')
loglog(fel_sekant_lista(1:end-1),fel_sekant_lista_iter,'m-') % Sekantmetoden i magenta
hold on
loglog(fel_newton_lista(1:end-1),fel_newton_lista_iter,'b-') % Newtons metod i blått