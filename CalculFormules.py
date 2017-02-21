import math

def ressort(e, v):
	return (1/3)*(e/(1-2*v))

def longueurAVide(lb, lc):
	return sqrt((lb**2)-((1/4)*lc**2))

def longueurDeplacement(lf, lv):
	return lf-lv

def masseProjectile(p, b, h, lf):
	return p*b*h*lf

def velocite(k, ld, mp):
	return sqrt((k*(ld**2))/mp)

def portee(v, g, a):
	return ((v**2)/g)*sin(2*a)

def energieImpact(mp, v):
	return (1/2)*mp*(v**2)

def equivalenceJouleGrammeTNT(ej):
	return ej/4184

def momentQuadratique(b, h):
	return (b*(h**3))/12

def forceTraction(k, lf):
	return k*lf

def resistanceFleche(f, lb, e, i):
	return (f*(lb**3))/(48*e*i)
