# -*- coding: utf-8 -*-
import sys
import math
import decimal
import re
import collections



atomC = ["C"+str(i) for i in range(1,6)]
atomH = ["H"+str(i) for i in range(6,16)]
atomO = ["O"+str(i) for i in range(16,20)]
atom = (atomC+atomH+atomO)
#print atom

# mass in a.u. 
mC=(12.0112E-3)/(6.023E23) 
mH=(1.0080E-3)/(6.023E23) 
mO=(15.9994E-3)/(6.023E23) 

totalM=float(mC*5+mH*10+mO*4)
def atom_Velocity():
    fp = open("D:/1.masterThesis/BACK_UP_RESULTS/SUGAR/K_Hole_Carbon/DoubleIon/doubleIon_with_core_5_10fs/K_Hole_C1/cpmd_12100/GEOMETRY_end_12100")
    d = {}
    i=0
    j=3
    for i, line in enumerate(fp):
        l = line.split()
        #print atom[i], l[3],l[4],l[5]
        atm = atom[i]
       
        if d.get(atm):
          d[atm].append(l[3:6])
        else:
          d[atm]=list(l[3:6])
          
        i+=1
              
    #print d
    fp.close()
    return d
d=atom_Velocity()

def list_append(lst, item):
  lst.append(item)
  return lst

def addMass():
    for k in d:
        #print d
        if k in atomC:
            d[k].append(mC)
        elif k in atomH:
            d[k].append(mH)
        elif k in atomO:
            d[k].append(mO)
        
    #print d
    return d
mV=addMass()
       



def sqr(y):
	f=math.pow
	return f(y,2)

'''Work here...'''
while True:
  frag_1=str(raw_input("Enter the atomic number to calculate kinetic energy of fragmentation part (eg. C5-O18-H13-H12-H11) :  "))
  f = frag_1.split('-')
  frag_part = [x.upper() for x in f]
  k=[i for i in frag_part if i not in atom]
  
  if any(k):
    print "You entered wrong fragmentation atom %s!!! Please enter again the correct fragmentation part.\n" %k
  else:
    #print "\n\nThe kinetic energy in kJ/mol for each atom is: \n\n"#, atom_kE 
    #print "\n\nThe Total Kinetic energy of your molecule is: %f kJ/mol or %f ev or %f kcal/mol ." % (total_KE, total_KE*96.48532324, total_KE*23.06054973) 
    #print "\n\nThe atoms for fragmentation part you entered are: ", frag_part  
    #part_KE = partKE(frag_part,atom_kE)  
    #print "\nThe Kinetic energy for fragmentation part is: %f kJ/mol or %f ev or %f kcal/mol ." % (part_KE, part_KE*96.48532324, part_KE*23.06054973)
    break

def partKE(frag_part, d):
  '''To calculate K.E. the fragmentation part:'''
  
  all_M=[]
  all_Vx=[]
  all_Vy=[]
  all_Vz=[]
  for k in frag_part:
    if k in d:
      #for key,(Vx, Vy, Vz) in d.items():
        #print key,(Vx, Vy, Vz)
        

        vx=float(d[k][0])
        vy=float(d[k][1])
        vz=float(d[k][2])
        m=float(d[k][3])
        
        #print vx, vy, vz
        #Covert vx to S.I. unit
        Vx=vx*2187691.2541
        Vy=vy*2187691.2541
        Vz=vz*2187691.2541
      #print d[k]
        #
        m_vx=m*Vx
        m_vy=m*Vy
        m_vz=m*Vz
        #print "m_vx", m_vx
        #print "m_vy", m_vy
        #print "m_vz", m_vz
        allM=list_append(all_M, m)      
        allVx=list_append(all_Vx, m_vx)
        allVy=list_append(all_Vy, m_vy)
        allVz=list_append(all_Vz, m_vz)

  #print all_M, all_Vx, all_Vy, all_Vz
  sumM=sum(all_M)
  #print "sumM=", sumM
  #sumM2=float(sqr(sumM))
  Vcm_x1=sum(all_Vx)
  Vcm_x=(Vcm_x1/sumM)
  #print "sum_Vx=", sum_Vx
  sumVcm_x=sqr(Vcm_x)
  #print "sumVx=", sumVx
  Vcm_y1=sum(all_Vy)
  Vcm_y=(Vcm_y1/sumM)
  sumVcm_y=sqr(Vcm_y)
  #print "sumVy=", sumVy
  Vcm_z1=sum(all_Vz)
  Vcm_z=(Vcm_z1/sumM)
  sumVcm_z=sqr(Vcm_z)
  #print "sumVz=", sumVz
  frag_Vcm=(sumVcm_x+sumVcm_y+sumVcm_z)
  frag_KE=(frag_Vcm*sumM)/2
  #print "frag_Vcm=", frag_Vcm
  #print "frag_KE=", frag_KE
  return frag_KE


part_K_E= partKE(frag_part, mV)
#part_KE=float(part_KE)

'''convert kinetic energy from joul to ev'''
part_KE = (part_K_E*6.241509E18)
print "\nThe Kinetic energy for fragmentation part (%s) is: %f kJ/mol or %f ev or %f kcal/mol ." % (frag_1, part_KE*96.485, part_KE, part_KE*23.06054973)

#To sum up all individual kinetic energy
#total_KE = sum(atom_kE.values())
def partKE2(frag_part, d):
  '''To calculate K.E. the fragmentation part:'''
  
  all_M=[]
  all_Vx=[]
  all_Vy=[]
  all_Vz=[]
  for k in d:
    if k not in frag_part:
      #for key,(Vx, Vy, Vz) in d.items():
        #print key,(Vx, Vy, Vz)
        

        vx=float(d[k][0])
        vy=float(d[k][1])
        vz=float(d[k][2])
        m=float(d[k][3])
        
        #print vx, vy, vz
        #Covert vx to S.I. unit
        Vx=vx*2187691.2541
        Vy=vy*2187691.2541
        Vz=vz*2187691.2541
      #print d[k]
        #
        m_vx=m*Vx
        m_vy=m*Vy
        m_vz=m*Vz
        #print "m_vx", m_vx
        #print "m_vy", m_vy
        #print "m_vz", m_vz
        allM=list_append(all_M, m)      
        allVx=list_append(all_Vx, m_vx)
        allVy=list_append(all_Vy, m_vy)
        allVz=list_append(all_Vz, m_vz)

  #print all_M, all_Vx, all_Vy, all_Vz
  sumM=sum(all_M)
  #print "sumM=", sumM
  #sumM2=float(sqr(sumM))
  Vcm_x1=sum(all_Vx)
  Vcm_x=(Vcm_x1/sumM)
  #print "sum_Vx=", sum_Vx
  sumVcm_x=sqr(Vcm_x)
  #print "sumVx=", sumVx
  Vcm_y1=sum(all_Vy)
  Vcm_y=(Vcm_y1/sumM)
  sumVcm_y=sqr(Vcm_y)
  #print "sumVy=", sumVy
  Vcm_z1=sum(all_Vz)
  Vcm_z=(Vcm_z1/sumM)
  sumVcm_z=sqr(Vcm_z)
  #print "sumVz=", sumVz
  frag_Vcm=(sumVcm_x+sumVcm_y+sumVcm_z)
  frag_KE=(frag_Vcm*sumM)/2
  #print "frag_Vcm=", frag_Vcm
  #print "frag_KE=", frag_KE
  return frag_KE


part_K_E2= partKE2(frag_part, mV)
#part_KE=float(part_KE)
other_part = [i for i in atom if i not in frag_part]
other_part2 = ('-'.join(map(str,other_part)))

'''convert kinetic energy from joul to ev'''
part_KE2 = (part_K_E2*6.241509E18)
print "\nThe Kinetic energy for other fragmentation part (%s) is: %f kJ/mol or %f ev or %f kcal/mol ." % (other_part2, part_KE2*96.485, part_KE2, part_KE2*23.06054973)


 




