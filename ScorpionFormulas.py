import math

def spring(e, v):
	return (1/3)*(e/(1-2*v))

def empty_length(lb, lc):
	formulas = (lb*lb)-((1/4)*lc*lc)
	if formulas > 0:
		result = math.sqrt(formulas)
	else:
		result = 0

	return result

def movement_length(lf, lv):
	return lf-lv

def projectile_mass(p, df, lf):
	return p*(math.pi)*(df/2)*(df/2)*lf

def velocity(k, ld, mp):
	return math.sqrt((k*(ld*ld))/mp)

def reach(v, g, a):
	return ((v*v)/g)*(math.sin(2*a))

def impact_energy(mp, v):
	return (1/2)*mp*(v*v)

def energy_grams_TNT(ej):
	return ej/4184

def quadratic_moment(b, h):
	return (b*(h*h*h))/12

def traction_force(k, ld):
	return k*ld

def arrow_arm_max(f, lb, e, i):
	return (f*(lb*lb*lb))/(48*e*i)
