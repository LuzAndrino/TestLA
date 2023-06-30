%LSA
%5/10/23
%following https://www.mathworks.com/help/matlab/matlab_prog/calculations-when-tables-have-both-numeric-and-nonnumeric-data.html#zmw57dd0e22901


a = readtable('thresholds_ger12to15.csv',"TextType","string");
a.pre_post = categorical(a.pre_post);
a.group = categorical(a.group);

response = a(:,5:end);

%a = renamevars(a, ["pre_post", "abr_type", "response_lvl"],["Pre or Post", "dB Level", "Threshold Response"]);

ger12 = a(1:12,["pre_post", "abr_type", "response_lvl"]);

x = ger12(["abr_type"]);
y = ger12(["response_lvl "]);
g = {a(["pre_post"])};

%Remove 16,20/Click,Chirp


