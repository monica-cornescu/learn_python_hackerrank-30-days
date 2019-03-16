c = ['la', 'le', 'li', 'me']

attemptLogin = "lalelilolulab"
for passw in c:
    passwordL = len(passw)
    startPoint = 0
    if attemptLogin.count(passw) > 0:
        passwIndex = 0
        while passwIndex >= 0:
            passwIndex = attemptLogin.find(passw, startPoint)
            print("passw %s is at index %d "% (passw, passwIndex))
            startPoint = passwIndex + passwordL


#attemptLogin = attemptLogin[(passwIndex + passwordL):]

