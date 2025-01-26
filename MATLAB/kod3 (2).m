%% uppgift 3a)
clc, clear

% Ladda in modellen eiffel1 som innehåller noder (xnod, ynod)
load('eiffel1.mat');

% Definiera antal noder i fackverket och välj den nod som ska belastas
antalet_noder = 261;  % Antalet noder i fackverket
nod = 261;  % Nodnummer att belasta

% Skapa en kraftvektor, b,  som är noll överallt utom på den valda
% noden, nod 261 
b = zeros(2 * antalet_noder, 1);  % Skapar en nollvektor som är dubbelt så lång som antalet noder (för både x- och y-komponenter), ***1 vid sidan är kolumnlängden***
b(nod * 2 - 1) = 1;  % Applicera en kraft i x-riktning på den valda noden (index nod*2-1 ger x-komponenten för noden)

% Lös ekvationssystemet A*x = b för att beräkna förskjutningarna av noderna
x = A \ b;  % Använd backslash (gausseliminering) för att lösa ekvationssystemet

% Beräkna nya koordinater för noderna efter att de har förskjutits
%xbel och ybel är nya koordinaterna efter kraftvektor förskjuter x och y noden.
xbel = xnod + x(1:2:end);  % Nya x-koordinater för noderna efter deformation, detta är den röda bilden
ybel = ynod + x(2:2:end);  % Nya y-koordinater för noderna efter deformation, detta är den röda bilden

% Skapa en ny figur för att plotta den deformerade strukturen
figure
hold on  % Håller kvar den ursprungliga strukturen så att vi kan plotta den nya ovanpå
trussplot(xnod, ynod, bars);  % Plotta ursprunglig struktur (i blått, standardfärg)
trussplot(xbel, ybel, bars, '-r');  % Plotta den deformerade strukturen (i rött)
plot(xbel(nod), ybel(nod), 'g*', 'MarkerSize', 15, 'LineWidth', 2);  % Markera den belastade noden med en stjärna för att visa dess nya position
legend('Original Struktur', 'Deformerad struktur', 'Belastad nod') 
title('Deformerad Struktur med Belastning på Nod 261');  % Titel för figuren
grid on;  % Lägg till ett rutnät för bättre visualisering
 % Lägg till en förklarande legend för varje plottad del
hold off  % Släpp kvarvarande plottar


%% uppgift 3b)
clc, clear

antal_noder = [261,399,561,1592]; %Antalet noder som finns i varje 
antal_okanda = 2.*antal_noder; %2 multiplicerat med antalet noder i modellen eftersom det är både (x,y) koordinater som är okända
hur_lang_tid = []; %Hur lång tid det tar
repetition = 10; %Den ska repetera 10 gånger för att få så bra värde som möjligt

for i = 1:length(antal_noder) %1 till 4 eftersom det finns 4 stycken och vi ska mäta tiden för varje
    load(['eiffel' num2str(i) '.mat']); %Number 2 str funktion
    b = randn(antal_okanda(i),1); %t.ex om det är randn(antal_okanda(1),1) så får vi ett random vektor varje repetition. Värdena är en random siffra av t.ex 261*2 i en kolumn
    full_tid = 0; %Initierar att tiden från början ska vara =0

    for k = 1:repetition % Upprepar beräkningarna
        tic %Tiden börjar tic
        x = A\b; %Själva gausseliminering
        full_tid = full_tid + toc; % Ackumulerad tid, toc gör så tiden stannar
    end
    
    genomsnittilig_tid = full_tid/repetition; %Genomsnittliga tiden för varje tic till toc eftersom jag tar fulltid/repetitionerna
    hur_lang_tid = [hur_lang_tid, genomsnittilig_tid];  

end

% Plottar tiden i förhållande till antal obekanta
loglog(antal_okanda, hur_lang_tid,'k-s')


%% uppgift 3c) För i) & ii)
clc, clear

antal_noder = [261, 399, 561, 1592];

% Funktion som utför metoden med LU-faktorisering
function [tid, svagaste_nod, starkaste_nod] = naiva_metoden(i, antal_noder)

    % Ladda modellens data
    load(['eiffel' num2str(i) '.mat']);
    tid=0;
    % Starta tidtagning för aktuell modell
    tic;
    % Antal noder i aktuell modell
    antal_noder = antal_noder(i);    
    % Initiera vektorn Tj med nollor för varje nod
    Tj = zeros(antal_noder, 1);   
    % Loopar över alla noder för att beräkna förskjutningen
    for j = 1:antal_noder
        b = zeros(2 * antal_noder, 1);
        b(2 * j) = -1; % Nedåtriktad kraft på aktuell nod
        xj = A\b;  
        % Beräkna normen av förskjutningsvektorn x_j
        Tj(j) = norm(xj);

    end 

    % Stoppa tidtagningen för aktuell modell
    tid = tid+toc;

    % Hitta den starkaste och svagaste noden baserat på Tj
    [~, starkaste_nod] = min(Tj);
    [~, svagaste_nod] = max(Tj);
    
    % Plotta strukturen och markera de starkaste och svagaste noderna
    figure(i); % Se till att en ny figur skapas för varje iteration
    trussplot(xnod, ynod, bars);
    hold on;
    plot(xnod(starkaste_nod), ynod(starkaste_nod), 'rO'); % Starkaste noden markeras med röd cirkel
    plot(xnod(svagaste_nod), ynod(svagaste_nod), 'b*'); % Svagaste noden markeras med blå stjärna
    hold off;
    drawnow; % Uppdatera figuren direkt, den poppar upp av sig själv
end

% Initialisera listor för att spara tidsmätningar och nodinformation
tidsmatning = [];
svag_nod_lista = [];
stark_nod_lista = [];

% Loop för att köra metoden med LU-faktorisering för varje modell och samla in resultat
for i = 1:length(antal_noder)
    fprintf('Bearbetar modell utifrån Naiv metod: %d av %d...\n', i, length(antal_noder)); % Statusutskrift
    [tidsmatning(i), svag_nod_lista(i), stark_nod_lista(i)] = naiva_metoden(i, antal_noder);
    fprintf('Modell %d av %d bearbetad. Det tog %.2f sekunder.\n', i, length(antal_noder), tidsmatning(i)); % Utskrift av tiden för varje modell
end



%% uppgift 3c) iii)
clc, clear

antal_noder = [261, 399, 561, 1592];

% Funktion som utför metoden med LU-faktorisering
function [tid, svagaste_nod, starkaste_nod] = lu_faktorisering(i, antal_noder)
    % Ladda modellens data
    load(['eiffel' num2str(i) '.mat']);    
    % Starta tidtagning
    tic;    
    % Utför LU-faktorisering av matrisen A
    [L, U] = lu(A);
    
    % Antal noder i aktuell modell
    antal_noder = antal_noder(i);
    
    % Initiera vektorn Tj med nollor för varje nod
    Tj = zeros(antal_noder, 1);
    
    % Loopar över alla noder för att beräkna förskjutningen
    for j = 1:antal_noder
        b = zeros(2 * antal_noder, 1);
        b(2 * j) = -1; % Nedåtriktad kraft på aktuell nod
        
        % Lös ekvationssystemet med hjälp av LU-faktoriseringen
        b_2 = L \ b; % Lös L * y = b och då får vi fram b_2 genom L\b
        xj = U \ b_2; % Lös U * xj = y, då får vi xj genom U\b_2
        
        % Beräkna normen av förskjutningsvektorn x_j
        Tj(j) = norm(xj);
    end

    % Stoppa tidtagningen
    tid = toc;

    % Hitta den starkaste och svagaste noden baserat på Tj
    [~, starkaste_nod] = min(Tj);
    [~, svagaste_nod] = max(Tj);
    
    % Plotta strukturen och markera de starkaste och svagaste noderna
    figure(i); % Se till att en ny figur skapas för varje iteration
    trussplot(xnod, ynod, bars);
    hold on;
    plot(xnod(starkaste_nod), ynod(starkaste_nod), 'rO'); % Starkaste noden markeras med röd cirkel
    plot(xnod(svagaste_nod), ynod(svagaste_nod), 'b*'); % Svagaste noden markeras med blå stjärna
    hold off;
    drawnow; % Uppdatera figuren direkt
end

% Initialisera listor för att spara tidsmätningar och nodinformation
tidsmatning = [];
svag_nod_lista = [];
stark_nod_lista = [];

% Loop för att köra metoden med LU-faktorisering för varje modell och samla in resultat
for i = 1:length(antal_noder)
    fprintf('Bearbetar modell utifrån LU-metoden: %d av %d\n', i, length(antal_noder)); % Statusutskrift
    [tidsmatning(i), svag_nod_lista(i), stark_nod_lista(i)] = lu_faktorisering(i, antal_noder);
     fprintf('Modell %d av %d bearbetad. Det tog %.2f sekunder.\n', i, length(antal_noder), tidsmatning(i)); % Utskrift av tiden för varje modell
end


%% uppgift 3c) iv) gles (ej LU)
clc, clear

antal_noder = [261, 399, 561, 1592];

% Funktion som utför metoden med LU-faktorisering
function [tid, svagaste_nod, starkaste_nod] = gles_naiva_metoden(i, antal_noder)
    % Ladda modellens data
    load(['eiffel' num2str(i) '.mat']);
    
    A=sparse(A);
    tid=0;
    % Starta tidtagning för aktuell modell
    tic;
    % Antal noder i aktuell modell
    antal_noder = antal_noder(i);
    
    % Initiera vektorn Tj med nollor för varje nod
    Tj = zeros(antal_noder, 1);
    
    % Loopar över alla noder för att beräkna förskjutningen
    for j = 1:antal_noder
        b = zeros(2 * antal_noder, 1);
        b(2 * j) = -1; % Nedåtriktad kraft på aktuell nod
        xj = A\b; 
        
        % Beräkna normen av förskjutningsvektorn x_j
        Tj(j) = norm(xj);
    end

    % Stoppa tidtagningen för aktuell modell
    tid = tid+toc;
    
    % Hitta den starkaste och svagaste noden baserat på Tj
    [~, starkaste_nod] = min(Tj);
    [~, svagaste_nod] = max(Tj);
    
    % Plotta strukturen och markera de starkaste och svagaste noderna
    figure(i); % Se till att en ny figur skapas för varje iteration
    trussplot(xnod, ynod, bars);
    hold on;
    plot(xnod(starkaste_nod), ynod(starkaste_nod), 'rO'); % Starkaste noden markeras med röd cirkel
    plot(xnod(svagaste_nod), ynod(svagaste_nod), 'b*'); % Svagaste noden markeras med blå stjärna
    hold off;
    drawnow; % Uppdatera figuren direkt
end

% Initialisera listor för att spara tidsmätningar och nodinformation
tidsmatning = [];
svag_nod_lista = [];
stark_nod_lista = [];

% Loop för att köra metoden med LU-faktorisering för varje modell och samla in resultat
for i = 1:length(antal_noder)
    fprintf('Bearbetar modell utifrån gles (ej LU): %d av %d...\n', i, length(antal_noder)); % Statusutskrift
    [tidsmatning(i), svag_nod_lista(i), stark_nod_lista(i)] = gles_naiva_metoden(i, antal_noder);
    fprintf('Modell %d av %d bearbetad. Det tog %.2f sekunder.\n', i, length(antal_noder), tidsmatning(i)); % Utskrift av tiden för varje modell
end


%% uppgift 3c) iv) gles och LU-faktorisering
clc, clear

antal_noder = [261, 399, 561, 1592];

% Funktion som utför metoden med LU-faktorisering
function [tid, svagaste_nod, starkaste_nod] = gles_lu_faktorisering(i, antal_noder)
    % Ladda modellens data
    load(['eiffel' num2str(i) '.mat']);
    A = sparse(A);
    
    % Utför LU-faktorisering av matrisen A
    [L, U] = lu(A);
    
    % Antal noder i aktuell modell
    antal_noder = antal_noder(i);
    
    % Initiera vektorn Tj med nollor för varje nod
    Tj = zeros(antal_noder, 1);

    % Starta tidtagning
    tic;
    % Loopar över alla noder för att beräkna förskjutningen
    for j = 1:antal_noder
        b = zeros(2 * antal_noder, 1);
        b(2 * j) = -1; % Nedåtriktad kraft på aktuell nod
        
        % Lös ekvationssystemet med hjälp av LU-faktoriseringen
        b_2 = L \ b; % Lös L * y = b
        xj = U \ b_2; % Lös U * x = y
        
        % Beräkna normen av förskjutningsvektorn x_j
        Tj(j) = norm(xj);
    end
    
    % Stoppa tidtagningen
    tid = toc;

    % Hitta den starkaste och svagaste noden baserat på Tj
    [~, starkaste_nod] = min(Tj);
    [~, svagaste_nod] = max(Tj);
    
    % Plotta strukturen och markera de starkaste och svagaste noderna
    figure(i); % Se till att en ny figur skapas för varje iteration
    trussplot(xnod, ynod, bars);
    hold on;
    plot(xnod(starkaste_nod), ynod(starkaste_nod), 'rO'); % Starkaste noden markeras med röd cirkel
    plot(xnod(svagaste_nod), ynod(svagaste_nod), 'b*'); % Svagaste noden markeras med blå stjärna
    hold off;
    drawnow; % Uppdatera figuren direkt
end

% Initialisera listor för att spara tidsmätningar och nodinformation
tidsmatning = [];
svag_nod_lista = [];
stark_nod_lista = [];

% Loop för att köra metoden med LU-faktorisering för varje modell och samla in resultat
for i = 1:length(antal_noder)
    fprintf('Bearbetar modell utifrån gles och LU-faktorisering: %d av %d\n', i, length(antal_noder)); % Statusutskrift
    [tidsmatning(i), svag_nod_lista(i), stark_nod_lista(i)] = gles_lu_faktorisering(i, antal_noder);
    fprintf('Modell %d av %d bearbetad. Det tog %.2f sekunder.\n', i, length(antal_noder), tidsmatning(i)); % Utskrift av tiden för varje modell
end