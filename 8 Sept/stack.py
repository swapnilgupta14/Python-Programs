#lex_auth_01269444890062848087

def find_correct(word_dict):
    c1,c2,c3,cou=0,0,0,0
    for i in word_dict:
        if(word_dict[i]==i):
            c1=c1+1
        elif(len(word_dict[i]!=len(i)):
            c3=c3+1
        else:
            x=word_dict[i]
            for j in range(len(x)):
                if(x[j]!=i[j]):
                    cou=cou+1
            if(cou<=2):
                c2+=1
            else:
                c3+=1
            cou=0
    list=[c1,c2,c3]
    return list