spin = input().strip()
charge = input().strip()

if spin == "1/2":
    if charge in ("-1/3", "2/3"):
        class_ = "Quark"
        if charge == "-1/3":
            particle = "Strange"
        elif charge == "2/3":
            particle = "Charm"
    elif charge in ("-1", "0"):
        class_ = "Lepton"
        if charge == "-1":
            particle = "Electron"
        elif charge == "0":
            particle = "Muon"
else:
    class_ = "Boson"
    particle = "Photon"

print(particle, class_)