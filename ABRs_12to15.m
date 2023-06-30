% LSA 5/2023
%Plot ABR Threshold levels 
%16 = click | 20 = chirp

%read in csv
a = readtable('thresholds_ger12to15.csv');
a.Properties.VariableNames = {'subject', 'group', 'pre_post', 'abr_type', 'response_lvl'};

ger12 = a(1:12,:);
ger15 = a(13:24,:);

ger13 = a(25:36,:);
ger14= a(37:end,:);

g12pre = a(1:6, :);
g12post = a(7:12,:);


%plot(ger12.abr_type, ger12.response_lvl, 'group',{'pre_post'};

nexttile
plot(g12pre.abr_type,g12pre.response_lvl)
title('Pre')

nexttile
plot(g12post.abr_type,g12post.response_lvl)
title('Post')

%do only frequencies! take out click and chirp and check out thats plotted
%in excel sheets
a = readtable('thresholds_ger12to15.csv',"TextType","string");
a.pre_post = categorical(a.pre_post);
a.group = categorical(a.group);
