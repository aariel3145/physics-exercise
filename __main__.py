

# all conversions assume one of the LHS equals the stored value of the RHS
kcal_ev = 2.611e22
joule_ev = 6.242e18
kcal_joule = 4184

# all comparisons below are in eV
planck_ev = 1.22e28
grandUnification_ev = 1e25
keMosquito_ev = 1e12
muonRest_ev = 105.7e6
ionizeH_ev = 13.6

# all comparisons below are in W
poe_w = 15.4
cpu_w = 60
stagelight_w = 750

cal_in = float(input("calories burned? "))
ev_burned = kcal_ev * cal_in
joule_burned = kcal_joule * cal_in
mins = float(input("minutes exercised? "))
sec = mins * 60.0
watt_burned = joule_burned / sec


print(f"equivalent energy: {ev_burned:.2e} eV")
print(f"\ttimes the Planck Energy: {ev_burned/planck_ev:.2e}")
print(f"\ttimes the Grand Unification Energy: {ev_burned/grandUnification_ev:.2e}")
print(f"\ttimes the kinetic energyt of a flying mosquito: {ev_burned/keMosquito_ev:.2e}")
print(f"\ttimes the muon rest energy: {ev_burned/muonRest_ev:.2e}")
print(f"\ttimes the energy required to ionize Hydrogen: {ev_burned/ionizeH_ev:.2e}")

print(f"equivalent power: {watt_burned:.2e} W [J/s]")
print(f"\ttimes incandescent stage light: {watt_burned/stagelight_w:.2e}")
print(f"\ttimes CPU draw: {watt_burned/cpu_w:.2e}")
print(f"\ttimes Class 0 POE: {watt_burned/poe_w:.2e}")
