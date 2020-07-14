def generate_hashtag(s):
    if len(s)<=0 or len(s)>=140:
      return False
    s=s.strip()
    k=""
    for i in range(len(s)):
      if i==0:
        k=k+s[i].upper()
        continue
      if i>0 and s[i-1]==" " and s[i]!=" ":
        k=k+s[i].upper()
      else:
        k=k+s[i].lower()
    k=k.replace(" ","")
    k="#"+k
    if(len(k)>140):
      return False
    else:
      return k


print(generate_hashtag("sujoydatta"))