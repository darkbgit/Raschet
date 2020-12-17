# -*- coding: utf-8 -*-


class data_in(object):
    name = str()
    steel = str()
    press = float()
    temp = int()
    sigma_d = float()
    dia = int()
    c_kor = float()
    c_minus = float()
    c_3=float(0)
    fi = float()
    s_prin = float()
    dav = str('vn')
    l = float()
    l3_1 = float(0)
    l3_2 = float(0)
    E = int()
    ny = float(2.4)
    met = str()
    elH = int()
    elh1 = int()
    alfa = int()
    yk = bool(False)

class data_out(object):
    s_calcr = float()
    s_calc = float()
    s_calcr1 = float()
    s_calcr2 = float()
    press_d = float()
    c = float()
    l = float()
    b = float()
    b_2 = float()
    b1 = float()
    b1_2 = float()
    press_dp = float()
    press_de = float()
    elR=float()
    elke = float()
    elx = float()
    err = str()
    ypf = bool()
    Dk = float()

class data_nozzlein(object):
    place = int()
    name = str()
    steel1 = str()
    steel2 = str()
    steel3 = str()
    steel4 = str()
    sigma_d1 = float()
    sigma_d2 = float()
    sigma_d3 = float()
    sigma_d4 = float()
    E1 = int()
    dia = int()
    s0 = float()
    s1 = float()
    s2 = float()
    s3 = float()
    cs = float()
    cs1 = float()
    l = int()
    l1 = int()
    l2 = int()
    l3 = int()
    fi = float()
    fi1 = float()
    delta = int()
    delta1 = int()
    delta2 = int()
    elx = int()
    b = float()
    vid = int()
    dav = str()
    met = str()
    ny = float(2.4)

class data_nozzleout(object):
    press_d = float()
    press_dp = float()
    press_de = float()
    Dp = float()
    dp = float()
    d0p = float()
    s1p = float()
    d0 = float()
    d01 = float()
    d02 = float()
    dmax = float()
    sp = float()
    spn = float()
    ppn = float()
    K1 = int()
    lp = float()
    l1p = float()
    l1p2 = float()
    l2p = float()
    l2p2 = float()
    l3p = float()
    l3p2 = float()
    L0 = float()
    psi1 = float()
    psi2 = float()
    psi3 = float()
    psi4 = float(1)
    b = float()
    V = float()
    V1 = float()
    V2 = float()
    yslyk1 = float()
    yslyk2 = float()
    B1n = float()
    pen = float()

class data_saddlein(object):
    G = int()
    L = int()
    Lob = int()
    H = int()
    e = float()
    a = float()
    p = float()
    D = float()
    s = float()
    s2 = float()
    c = float()
    fi = float()
    sigma_d = float()
    E = int()
    ny = float(2.4)
    type = int()
    b = float()
    b2 = float()
    delta1 = int()
    delta2 = int()
    name = str()
    nameob = str()
    temp = int()
    l0 = int()
    steel = str()

class data_saddleout(object):
    q = float()
    M0 = float()
    p_d = float()
    F1 = float()
    F2 = float()
    F_d = float()
    M1 = float()
    M2 = float()
    M12 = float()
    M_d = float()
    Q1 = float()
    Q2 = float()
    Q_d = float()
    B1 = float()
    B1_2 = float()
    yslproch1_1 = float()
    yslproch1_2 = float()
    yslproch2 = float()
    yslystoich1 = float()
    yslystoich2 = float()
    K9 = float()
    K9_1 = float()
    y = float()
    x = float()
    gamma = float()
    beta1 = float()
    K10 = float()
    K10_1 = float()
    K11 = float()
    K12 = float()
    K13 = float()
    K14 = float()
    K15 = float()
    K15_2 = float()
    K16 = float()
    K17 = float()
    sigma_mx = float()
    F_d2 = float()
    F_d3 = float()
    v1_2 = float()
    v1_3 = float()
    v21_2 = float()
    v21_3 = int(0)
    v22_2 = float()
    v22_3 = float()
    K2 = float()
    K1_2 = float()
    K1_21 = float()
    K1_22 = float()
    K1_3 = float()
    K1_31 = float()
    K1_32 = float()
    sigmai2 = float()
    sigmai2_1 = float()
    sigmai2_2 = float()
    sigmai3 = float()
    sigmai3_1 = float()
    sigmai3_2 = float()
    Fe = float()
    sef = float()

class data_heatin(object):
    a = float()
    a1 = float()

class data_heatout(object):
    mn = float()








class CalcClass(object):
    """description of class"""

    import json
    import data_fiz
    import math

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    


    
    def get_sigma(self, name, temp, tolst='', dva=''):
        """ 
        Get sigma from steel and temp
        name - steel
        temp - temperature Celsius deegre
        tolst - big thicknes '-b'
        dva - big period '-2'
        """
        name = name + tolst + dva
      #  keys = data_fiz.sigma_list.keys()
        if name in self.data_fiz.sigma_list.keys():
            for t in self.data_fiz.sigma_list[name]:
                if temp == t['temp']:
                    sigma = t['sigma']
                    break
                elif temp > t['temp']:
                    temp_l = t['temp']
                    sigma_b = t['sigma'] 
                    continue
                else:
                    temp_b = t['temp']
                    sigma_l = t['sigma']
                    sigma = sigma_b - ((sigma_b-sigma_l)*(temp-temp_l)/(temp_b-temp_l))
                    sigma = round(sigma, 1)
                    sigma_str = str(sigma).split('.')
                    if sigma_str[1] > '5':
                        sigma_str[1] = '5'
                        sigma = float('.'.join(sigma_str))
                    elif sigma_str[1] < '5':
                        sigma_str[1] = '0'
                        sigma = float('.'.join(sigma_str))
                
                    break
            return sigma
        else:
            return f'Сталь {name} не найдена'


    def get_E(self, name, temp):
        """ 
        Get E from steel and temp
        name - steel
        temp - temperature Celsius deegre
        """
        import re
        f = re.findall(r'(.*)(?:\()', name, re.S)
        if f != []:
            name = f[0]

        for a in self.data_fiz.class_list.keys():
            if name in self.data_fiz.class_list[a]:
                for t in self.data_fiz.E_list[a]:
                    if temp == t['temp']:
                        E = t['E']
                        break
                    elif temp > t['temp']:
                        temp_l = t['temp']
                        E_b = t['E'] 
                        continue
                    else:
                        temp_b = t['temp']
                        E_l = t['E']
                        E = E_b - ((E_b-E_l)*(temp-temp_l)/(temp_b-temp_l))
                        E = int(round(E, 0))
                        break
                return E
                break
            #else:
            #    return f'Сталь {name} не найдена'



    def calc_ob(self, data_in:data_in):
        """ 
        in data_in(name, steel, press, temp, sigma_d, 
            dia, c_kor, c_minus, fi, s_prin,
            dav - 'vn' or 'nar'
            l=0 ,l3_1=0, l3_2=0 E=0)
          out data_out [0] - s_calcr [1] - s_calc [2] - s_prin [3] - press_d [4] - c
        """
        
        import math
        
        do_out = data_out()

        do_out.c = data_in.c_kor + data_in.c_minus + data_in.c_3
        if ((data_in.dia < 200) and ((data_in.s_prin - do_out.c)/data_in.dia <= 0.3)) or ((data_in.dia >= 200) and ((data_in.s_prin - do_out.c)/data_in.dia <= 0.3)):
            do_out.ypf = True
        else:
            do_out.ypf = False

        if data_in.dav == 'vn':
            do_out.s_calcr = data_in.press * data_in.dia / ((2 * data_in.sigma_d * data_in.fi) - data_in.press)
            
            do_out.s_calc = do_out.s_calcr + do_out.c

            if data_in.s_prin == 0.0:
                do_out.press_d = 2 * data_in.sigma_d * data_in.fi * (do_out.s_calc - do_out.c) / (data_in.dia + do_out.s_calc - do_out.c)
            elif data_in.s_prin > do_out.s_calc:
                do_out.press_d = 2 * data_in.sigma_d * data_in.fi * (data_in.s_prin - do_out.c) / (data_in.dia + data_in.s_prin - do_out.c)
            else:
                do_out.err = 'Принятая толщина меньше расчетной'
            return do_out
        elif data_in.dav == 'nar':
            do_out.l = data_in.l + data_in.l3_1 + data_in.l3_2
            do_out.b_2 = 0.47*math.pow((data_in.press/(0.00001*data_in.E)),0.067)*math.pow(do_out.l/data_in.dia,0.4)
            do_out.b = max(1.0, do_out.b_2)
            do_out.s_calcr1 = 1.06 * (0.01 * data_in.dia / do_out.b) * math.pow((data_in.press/(0.00001*data_in.E))*(do_out.l/data_in.dia), 0.4)
            do_out.s_calcr2 = 1.2*data_in.press*data_in.dia/(2*data_in.sigma_d-data_in.press)
            do_out.s_calcr = max(do_out.s_calcr1, do_out.s_calcr2)
            
            do_out.s_calc = do_out.s_calcr + do_out.c
            if data_in.s_prin == 0.0:
                do_out.press_dp = 2*data_in.sigma_d*(do_out.s_calc-do_out.c)/(data_in.dia+do_out.s_calc-do_out.c)
                do_out.b1_2 = 9.45*(data_in.dia/do_out.l)*math.sqrt(data_in.dia/(100*(do_out.s_calc-do_out.c)))
                do_out.b1 = max(1.0, do_out.b1_2)
                do_out.press_de = ((2.08*0.00001*data_in.E)/data_in.ny*do_out.b1)*(data_in.dia/do_out.l)*math.pow(100*(do_out.s_calc-do_out.c)/data_in.dia,2.5)
                do_out.press_d = do_out.press_dp/math.sqrt(1+math.pow(do_out.press_dp/do_out.press_de,2))
            elif data_in.s_prin > do_out.s_calc:
                do_out.press_dp = 2*data_in.sigma_d*(data_in.s_prin-do_out.c)/(data_in.dia+data_in.s_prin-do_out.c)
                do_out.b1_2 = 9.45*(data_in.dia/do_out.l)*math.sqrt(data_in.dia/(100*(data_in.s_prin-do_out.c)))
                do_out.b1 = min(1.0, do_out.b1_2)
                do_out.press_de = ((2.08*0.00001*data_in.E)/data_in.ny*do_out.b1)*(data_in.dia/do_out.l)*math.pow(100*(data_in.s_prin-do_out.c)/data_in.dia,2.5)
                do_out.press_d = do_out.press_dp/math.sqrt(1+math.pow(do_out.press_dp/do_out.press_de,2))
            else:
                do_out.err = 'Принятая толщина меньше расчетной'
            return do_out




        else:
            return 'Dont true'


    def calc_el(self, data_in:data_in): 
        
        
        import math
        
        do_out = data_out()


        do_out.c = data_in.c_kor + data_in.c_minus + data_in.c_3
        if  (0.002 <= ((data_in.s_prin - data_out.c)/data_in.dia) <= 0.1) and (0.2 <= (data_in.elH/data_in.dia) < 0.5):
            do_out.ypf = True
        else:
            do_out.ypf = False
                    

        do_out.elR = math.pow(data_in.dia, 2)/(4*data_in.elH)
        if data_in.dav == 'vn':
            
            do_out.s_calcr = data_in.press * do_out.elR / ((2 * data_in.sigma_d * data_in.fi) - 0.5 * data_in.press)
            
            do_out.s_calc = do_out.s_calcr + do_out.c

            if data_in.s_prin == 0.0:
                do_out.press_d = 2 * data_in.sigma_d * data_in.fi * (do_out.s_calc - do_out.c) / (do_out.elR + 0.5 * (do_out.s_calc - do_out.c))
            elif data_in.s_prin > do_out.s_calc:
                do_out.press_d = 2 * data_in.sigma_d * data_in.fi * (data_in.s_prin - do_out.c) / (do_out.elR + 0.5 * (do_out.s_calc - do_out.c))
            else:
                do_out.err = 'Принятая толщина меньше расчетной'
            return do_out
        elif data_in.dav == 'nar':
            
            do_out.s_calcr2 = 1.2*data_in.press*do_out.elR/(2*data_in.sigma_d)
                        
            do_out.elke = 0.9 # добавить ке для полусферических =1
            do_out.s_calcr1 = (do_out.elke * do_out.elR) / 161 * math.sqrt((data_in.ny * data_in.press) / (0.00001*data_in.E))
            do_out.s_calcr = max(do_out.s_calcr1, do_out.s_calcr2)
            do_out.s_calc = do_out.s_calcr + do_out.c
            if data_in.s_prin == 0.0:
                do_out.elke = 0.9 # добавить ке для полусферических =1
                do_out.s_calcr1 = (do_out.elke * do_out.elR) / 161 * math.sqrt((data_in.ny * data_in.press) / (0.00001*data_in.E))
                do_out.s_calcr = max(do_out.s_calcr1, do_out.s_calcr2)
                #do_out.press_dp = 2*data_in.sigma_d*(do_out.s_calc-do_out.c)/(do_out.elR + 0.5 * (do_out.s_calc-do_out.c))
                #do_out.elx = 10 * ((data_in.s_prin-do_out.c)/data_in.dia)*(data_in.dia/(2*data_in.elH)-(2*data_in.elH)/data_in.dia)
                #do_out.elke = (1 + (2.4 + 8 * do_out.elx)*do_out.elx)/(1+(3.0+10*do_out.elx)*do_out.elx)
                #do_out.press_de = (2.6*0.00001*data_in.E)/data_in.ny*math.pow(100*(do_out.s_prin-do_out.c)/(do_out.elke*do_out.elR,2))
                #do_out.press_d = do_out.press_dp/math.sqrt(1+math.pow(do_out.press_dp/do_out.press_de,2))
            elif data_in.s_prin > do_out.s_calc:
                do_out.press_dp = 2*data_in.sigma_d*(data_in.s_prin-do_out.c)/(do_out.elR + 0.5 * (data_in.s_prin-do_out.c))
                do_out.elx = 10 * ((data_in.s_prin-do_out.c)/data_in.dia)*(data_in.dia/(2*data_in.elH)-(2*data_in.elH)/data_in.dia)
                do_out.elke = (1 + (2.4 + 8 * do_out.elx)*do_out.elx)/(1+(3.0+10*do_out.elx)*do_out.elx)
                do_out.press_de = (2.6*0.00001*data_in.E)/data_in.ny*math.pow(100*(data_in.s_prin-do_out.c)/(do_out.elke*do_out.elR),2)
                do_out.press_d = do_out.press_dp/math.sqrt(1+math.pow(do_out.press_dp/do_out.press_de,2))
            else:
                do_out.err = 'Принятая толщина меньше расчетной'
            return do_out




        else:
            return 'Dont true'


    def calc_nozzle(self, data_in:data_in, data_out:data_out, data_nozzlein:data_nozzlein):
        import math
        
        do_out = data_nozzleout()
        # расчет Dp, dp
        if data_in.met == 'obvn' or data_in.met == 'obnar':
            do_out.Dp = data_in.dia

            if data_nozzlein.place == 1: #Radial
                do_out.dp = data_nozzlein.dia + 2 * data_nozzlein.cs
            elif data_nozzlein.place == 2: #'Axial'
                pass
            elif data_nozzlein.place == 3: #'Offset'
                pass
            elif data_nozzlein.place == 4: #'Tilted'
                pass
        elif data_in.met == 'konvn' or data_in.met == 'konnar':
            do_out.Dp = data_out.Dk/(math.cos(math.radians(data_in.alfa)))
        elif data_in.met == 'elvn' or data_in.met == 'elnar':
            if data_in.elH == data_in.dia * 0.25:
                do_out.Dp = data_in.dia*2*math.sqrt(1 - 3*(math.pow(data_nozzlein.elx/data_in.dia, 2)))
            else:
                do_out.Dp = (data_in.dia ** 2)/(data_in.elH * 2) * math.sqrt(1 - (4 * ((data_in.dia ** 2) - 4 * (data_in.elH ** 2)) * (data_nozzlein.elx ** 2))/(data_in.dia ** 4))

            if data_nozzlein.place == 1: #Radial
                do_out.dp = data_nozzlein.dia + 2 * data_nozzlein.cs
            elif data_nozzlein.place == 2: #'Axial'
                pass
            elif data_nozzlein.place == 3: #'Offset'
                pass
            elif data_nozzlein.place == 4: #'Tilted'
                pass


        do_out.s1p = data_in.press*(data_nozzlein.dia+2*data_nozzlein.cs)/(2*data_nozzlein.fi*data_nozzlein.sigma_d1-data_in.press)

        
        # l1p, l3p, l2p
        do_out.l1p2 = 1.25*math.sqrt((data_nozzlein.dia+2*data_nozzlein.cs)*(data_nozzlein.s1-data_nozzlein.cs))
        do_out.l1p = min(data_nozzlein.l1, do_out.l1p2)
        if data_nozzlein.s3 == 0:
            do_out.l3p = 0
        else:
            do_out.l3p2 = 0.5*math.sqrt((data_nozzlein.dia+2*data_nozzlein.cs)*(data_nozzlein.s3-data_nozzlein.cs-data_nozzlein.cs1))
            do_out.l3p = min(data_nozzlein.l3, do_out.l3p2)

        do_out.L0 = math.sqrt(do_out.Dp*(data_in.s_prin-data_out.c))

        if data_nozzlein.vid in [1, 2, 3, 4, 5, 6]:
            do_out.lp = do_out.L0
        elif data_nozzlein.vid in [7, 8]:
            do_out.lp = min(data_nozzlein.l, do_out.L0)

        do_out.l2p2 = math.sqrt(do_out.Dp*(data_nozzlein.s2 + data_in.s_prin - data_out.c))
        do_out.l2p = min(data_nozzlein.l2, do_out.l2p2)

        
        if data_nozzlein.vid in [1, 2, 3, 4, 5, 6]:
            data_nozzlein.s0 = data_in.s_prin
            data_nozzlein.steel4 = data_nozzlein.steel1

        data_nozzlein.sigma_d2 = self.get_sigma(data_nozzlein.steel2, data_in.temp)
        data_nozzlein.sigma_d3 = self.get_sigma(data_nozzlein.steel3, data_in.temp)
        data_nozzlein.sigma_d4 = self.get_sigma(data_nozzlein.steel4, data_in.temp)

        do_out.psi1 = min(1, data_nozzlein.sigma_d1/data_in.sigma_d)
        do_out.psi2 = min(1, data_nozzlein.sigma_d2/data_in.sigma_d)
        do_out.psi3 = min(1, data_nozzlein.sigma_d3/data_in.sigma_d)
        do_out.psi4 = min(1, data_nozzlein.sigma_d4/data_in.sigma_d)

        do_out.d0p = 0.4*math.sqrt(do_out.Dp*(data_in.s_prin-data_out.c))

        do_out.b = math.sqrt(do_out.Dp*(data_in.s_prin-data_out.c)) + math.sqrt(do_out.Dp*(data_in.s_prin-data_out.c))
        
        if data_in.met == 'obvn' or data_in.met == 'obnar':
            do_out.sp = data_out.s_calcr
                                    
            do_out.dmax = data_in.dia
            do_out.K1 = 1
            if data_in.met == 'obvn':
                do_out.spn = data_out.s_calcr
            else:
                do_out.B1n = min(1, 9.45*(data_in.dia/data_out.l)*math.sqrt(data_in.dia/(100*(data_in.s_prin-data_out.c))))
                do_out.pen = 2.08*0.00001*data_in.E/(data_nozzlein.ny*do_out.B1n)*(data_in.dia/data_out.l)*math.pow(100*(data_in.s_prin-data_out.c)/data_in.dia,2.5)
                do_out.ppn = data_in.press/math.sqrt(1-math.pow(data_in.press/do_out.pen, 2))
                do_out.spn = do_out.ppn*do_out.Dp/(2*do_out.K1*data_in.sigma_d-do_out.ppn)
            

            

            
        elif data_in.met == 'konvn' or data_in.met == 'konnar':
            pass


        elif data_in.met == 'elvn' or data_in.met == 'elnar':
            
            if data_in.met == 'elvn':
               do_out.sp = data_in.press*do_out.Dp/(2*data_nozzlein.fi*data_in.sigma_d-data_in.press)
            elif data_in.met == 'elnar':
                do_out.sp = data_out.s_calcr

            do_out.dmax = 0.6 * data_in.dia
            do_out.K1 = 2
            if data_in.met == 'elvn':
                do_out.spn = do_out.sp
            elif data_in.met == 'elnar':
                do_out.B1n = min(1, 9.45*(data_in.dia/data_out.l)*math.sqrt(data_in.dia/(100*(data_in.s_prin-data_out.c))))
                do_out.pen = 2.08*0.00001*data_in.E/(data_nozzlein.ny*do_out.B1n)*(data_in.dia/data_out.l)*math.pow(100*(data_in.s_prin-data_out.c)/data_in.dia,2.5)
                do_out.ppn = data_in.press/math.sqrt(1-math.pow(data_in.press/do_out.pen, 2))
                do_out.spn = do_out.ppn*do_out.Dp/(2*do_out.K1*data_in.sigma_d-do_out.ppn)

       

        do_out.d01 = 2*((data_in.s_prin-data_out.c)/do_out.spn - 0.8)*math.sqrt(do_out.Dp*(data_in.s_prin-data_out.c))
        do_out.d02 = do_out.dmax+2*data_nozzlein.cs
        do_out.d0 = min(do_out.d01,do_out.d02)

        if do_out.dp > do_out.d0:
            do_out.yslyk1 = do_out.l1p*(data_nozzlein.s1-do_out.s1p-data_nozzlein.cs)*do_out.psi1 + do_out.l2p*data_nozzlein.s2*do_out.psi2 + do_out.l3p*(data_nozzlein.s3-data_nozzlein.cs-data_nozzlein.cs1)*do_out.psi3+do_out.lp*(data_in.s_prin-data_out.s_calcr-data_out.c)*do_out.psi4
            do_out.yslyk2 = 0.5*(do_out.dp-do_out.d0p)*data_out.s_calcr
        
        do_out.V1 = (data_nozzlein.s0-data_out.c)/(data_in.s_prin-data_out.c)
        do_out.V2 = (do_out.psi4 + (do_out.l1p*(data_nozzlein.s1-data_nozzlein.cs)*do_out.psi1 + do_out.l2p*data_nozzlein.s2*do_out.psi2 + do_out.l3p*(data_nozzlein.s3-data_nozzlein.cs-data_nozzlein.cs1)*do_out.psi3)/do_out.lp*(data_in.s_prin-data_out.c))/(1+0.5*(do_out.dp-do_out.d0p)/do_out.lp + do_out.K1*(data_nozzlein.dia+2*data_nozzlein.cs)/do_out.Dp*(data_nozzlein.fi/data_nozzlein.fi1)*(do_out.l1p/do_out.lp))
        do_out.V = min(do_out.V1, do_out.V2)

        if data_in.dav == 'vn':
            do_out.press_d = 2*do_out.K1*data_nozzlein.fi*data_in.sigma_d*(data_in.s_prin-data_out.c)*do_out.V/(do_out.Dp+(data_in.s_prin-data_out.c)*do_out.V)
        elif data_in.dav == 'nar':
            do_out.press_dp = 2*do_out.K1*data_nozzlein.fi*data_in.sigma_d*(data_in.s_prin-data_out.c)*do_out.V/(do_out.Dp+(data_in.s_prin-data_out.c)*do_out.V)
            do_out.press_de = data_out.press_de
            do_out.press_d = do_out.press_dp/math.sqrt(1+math.pow(do_out.press_dp/do_out.press_de,2))
        
            
        

        return (do_out)


    def calc_saddle(self, d_sin:data_saddlein):
        import math
        d_sin.sigma_d = self.get_sigma(d_sin.steel, d_sin.temp)
        d_sin.E = self.get_E(d_sin.steel, d_sin.temp)
        do_out = data_saddleout()

        do_out.M_d = (0.0000089*d_sin.E)/d_sin.ny*math.pow(d_sin.D, 3)*math.pow((100*(d_sin.s-d_sin.c))/d_sin.D, 2.5)
        #проверить формулу для расчета [F]
        do_out.F_d = (0.0000031*d_sin.E)/d_sin.ny*math.pow(d_sin.D, 2)*math.pow((100*(d_sin.s-d_sin.c))/d_sin.D, 2.5)
        do_out.Q_d = (2.4*d_sin.E*math.pow(d_sin.s-d_sin.c, 2))/d_sin.ny*(0.18+3.3*d_sin.D*(d_sin.s-d_sin.c))/math.pow(d_sin.L, 2)
        do_out.B1_2 = 9.45*(d_sin.D/d_sin.L)*math.sqrt(d_sin.D/(100*(d_sin.s-d_sin.c)))
        do_out.B1 = min(1, do_out.B1_2)
        do_out.p_d = (0.00000208*d_sin.E)/(d_sin.ny*do_out.B1)*(d_sin.D/d_sin.L)*math.pow((100*(d_sin.s-d_sin.c))/d_sin.D, 2.5)
        
        do_out.q = d_sin.G/(d_sin.L+(4/3)*d_sin.H)
        do_out.M0 = do_out.q*(math.pow(d_sin.D, 2)/16)
        do_out.F1 = d_sin.G/2
        do_out.F2 = do_out.F1
        do_out.M1 = do_out.q*math.pow(d_sin.e, 2)/2-do_out.M0
        do_out.M2 = do_out.M1
        do_out.M12 = do_out.M0 + do_out.F1*(d_sin.L/2-d_sin.a)-(do_out.q/2)*math.pow(d_sin.L/2+(2/3)*d_sin.H, 2)
        do_out.Q1 = (d_sin.L-2*d_sin.a)*do_out.F1/(d_sin.L+(4/3)*d_sin.H)
        do_out.Q2 = do_out.Q1
        if do_out.M12 > do_out.M1:
            do_out.y = d_sin.D/(d_sin.s-d_sin.c)
            do_out.x = d_sin.L/d_sin.D
            do_out.K9_1 = 1.6-0.20924*(do_out.x-1)+0.028702*do_out.x*(do_out.x-1)+0.0004795*do_out.y*(do_out.x-1)-0.0000002391*do_out.x*do_out.y*(do_out.x-1)-0.0029936*(do_out.x-1)*math.pow(do_out.x, 2)-0.00000085692*(do_out.x-1)*math.pow(do_out.y, 2)+0.00000088174*math.pow(do_out.x, 2)*(do_out.x-1)*do_out.y-0.0000000075955*math.pow(do_out.y, 2)*(do_out.x-1)*do_out.x+0.000082748*(do_out.x-1)*math.pow(do_out.x, 3)+0.00000000048168*(do_out.x-1)*math.pow(do_out.y, 3)
            do_out.K9 = max(do_out.K9_1, 1)
            do_out.yslproch1_1 = d_sin.p*d_sin.D/(4*(d_sin.s-d_sin.c))+4*do_out.M12*do_out.K9/(math.pi*math.pow(d_sin.D, 2)*(d_sin.s-d_sin.c))
            do_out.yslproch1_2 = d_sin.sigma_d*d_sin.fi
            if d_sin.dav == 'vn':
                do_out.yslystoich1 = do_out.M12/do_out.M_d
            elif d_sin.dav == 'nar':
                do_out.yslystoich1 = d_sin.p/do_out.p_d+do_out.M12/do_out.M_d
        if d_sin.type == 1:
            do_out.gamma = 2.83*(d_sin.a/d_sin.D)*math.sqrt((d_sin.s-d_sin.c)/d_sin.D)
            do_out.beta1 = 0.91*d_sin.b/math.sqrt(d_sin.D*(d_sin.s-d_sin.c))
            do_out.K10_1 = math.exp(-do_out.beta1)*math.sin(do_out.beta1)/do_out.beta1
            do_out.K10 = max(do_out.K10_1, 0.25)
            do_out.K11 = (1-math.exp(-do_out.beta1)*math.cos(do_out.beta1))/do_out.beta1
            do_out.K12 = (1.15-0.1432*math.radians(d_sin.delta1))/math.sin(0.5*math.radians(d_sin.delta1))
            do_out.K13 = max(1.7-2.1*math.radians(d_sin.delta1)/math.pi,0)/math.sin(0.5*math.radians(d_sin.delta1))
            do_out.K14 = (1.45-0.43*math.radians(d_sin.delta1))/math.sin(0.5*math.radians(d_sin.delta1))
            do_out.K15_2 = (0.8*math.sqrt(do_out.gamma)+6*do_out.gamma)/math.radians(d_sin.delta1)
            do_out.K15 = min(1, do_out.K15_2)
            do_out.K16 = 1-0.65/(1+math.pow(6*do_out.gamma, 2))*math.sqrt(math.pi/(3*math.radians(d_sin.delta1)))
            do_out.K17 = 1/(1+0.6*math.pow(d_sin.D/(d_sin.s-d_sin.c), 1/3)*(d_sin.b/d_sin.D)*math.radians(d_sin.delta1))
            do_out.sigma_mx = 4*do_out.M1/(math.pi*math.pow(d_sin.D, 2)*(d_sin.s-d_sin.c))

            do_out.v1_2 = -0.23*do_out.K13*do_out.K15/(do_out.K12*do_out.K10)
            do_out.v1_3 = -0.53*do_out.K11/(do_out.K14*do_out.K16*do_out.K17*math.sin(0.5*math.radians(d_sin.delta1)))
            
            do_out.K2 = 1.25 # добавить для условий монтажа
            do_out.v21_2 = -do_out.sigma_mx/(do_out.K2*d_sin.sigma_d)
            do_out.v21_3 = 0
            do_out.v22_2 = ((d_sin.p*d_sin.D)/(4*(d_sin.s-d_sin.c))-do_out.sigma_mx)/(do_out.K2*d_sin.sigma_d)
            do_out.v22_3 = ((d_sin.p*d_sin.D)/(2*(d_sin.s-d_sin.c)))/(do_out.K2*d_sin.sigma_d)

            do_out.K1_21 = (1-math.pow(do_out.v21_2, 2))/((1/3+do_out.v1_2*do_out.v21_2)+math.sqrt(math.pow(1/3+do_out.v1_2*do_out.v21_2, 2)+(1-math.pow(do_out.v21_2, 2))*math.pow(do_out.v1_2, 2)))
            do_out.K1_22 = (1-math.pow(do_out.v22_2, 2))/((1/3+do_out.v1_2*do_out.v22_2)+math.sqrt(math.pow(1/3+do_out.v1_2*do_out.v22_2, 2)+(1-math.pow(do_out.v22_2, 2))*math.pow(do_out.v1_2, 2)))
            do_out.K1_2 = min(do_out.K1_21, do_out.K1_22)

            do_out.K1_31 = (1-math.pow(do_out.v21_3, 2))/((1/3+do_out.v1_3*do_out.v21_3)+math.sqrt(math.pow(1/3+do_out.v1_3*do_out.v21_3, 2)+(1-math.pow(do_out.v21_3, 2))*math.pow(do_out.v1_3, 2)))
            do_out.K1_32 = (1-math.pow(do_out.v22_3, 2))/((1/3+do_out.v1_3*do_out.v22_3)+math.sqrt(math.pow(1/3+do_out.v1_3*do_out.v22_3, 2)+(1-math.pow(do_out.v22_3, 2))*math.pow(do_out.v1_3, 2)))
            do_out.K1_3 = min(do_out.K1_31, do_out.K1_32)

            do_out.sigmai2_1 = do_out.K1_21*do_out.K2*d_sin.sigma_d
            do_out.sigmai2_2 = do_out.K1_22*do_out.K2*d_sin.sigma_d
            do_out.sigmai2 = min(do_out.sigmai2_1, do_out.sigmai2_2)

            do_out.sigmai3_1 = do_out.K1_31*do_out.K2*d_sin.sigma_d
            do_out.sigmai3_2 = do_out.K1_32*do_out.K2*d_sin.sigma_d
            do_out.sigmai3 = min(do_out.sigmai3_1, do_out.sigmai3_2)

            do_out.F_d2 = 0.7*do_out.sigmai2*(d_sin.s-d_sin.c)*math.sqrt(d_sin.D*(d_sin.s-d_sin.c))/(do_out.K10*do_out.K12)
            do_out.F_d3 = 0.9*do_out.sigmai3*(d_sin.s-d_sin.c)*math.sqrt(d_sin.D*(d_sin.s-d_sin.c))/(do_out.K14*do_out.K16*do_out.K17)

            do_out.Fe = do_out.F1*(math.pi/4)*do_out.K13*do_out.K15*math.sqrt(d_sin.D/(d_sin.s-d_sin.c))

            if d_sin.dav == 'vn':
                do_out.yslystoich2 = do_out.M1/do_out.M_d+do_out.Fe/do_out.F_d+math.pow(do_out.Q1/do_out.Q_d, 2)
            elif d_sin.dav == 'nar':
                do_out.yslystoich2 = d_sin.p/do_out.p_d+do_out.M1/do_out.M_d+do_out.Fe/do_out.F_d+math.pow(do_out.Q1/do_out.Q_d, 2)

        elif d_sin.type == 2:
            do_out.sef = (d_sin.s- d_sin.c)*math.sqrt(1+math.pow(d_sin.s2/(d_sin.s- d_sin.c),2))
            do_out.gamma = 2.83*(d_sin.a/d_sin.D)*math.sqrt((do_out.sef)/d_sin.D)
            do_out.beta1 = 0.91*d_sin.b2/math.sqrt(d_sin.D*(do_out.sef))
            do_out.K10_1 = math.exp(-do_out.beta1)*math.sin(do_out.beta1)/do_out.beta1
            do_out.K10 = max(do_out.K10_1, 0.25)
            do_out.K11 = (1-math.exp(-do_out.beta1)*math.cos(do_out.beta1))/do_out.beta1
            do_out.K12 = (1.15-0.1432*math.radians(d_sin.delta2))/math.sin(0.5*math.radians(d_sin.delta2))
            do_out.K13 = max(1.7-2.1*math.radians(d_sin.delta2)/math.pi,0)/math.sin(0.5*math.radians(d_sin.delta2))
            do_out.K14 = (1.45-0.43*math.radians(d_sin.delta2))/math.sin(0.5*math.radians(d_sin.delta2))
            do_out.K15_2 = (0.8*math.sqrt(do_out.gamma)+6*do_out.gamma)/math.radians(d_sin.delta2)
            do_out.K15 = min(1, do_out.K15_2)
            do_out.K16 = 1-0.65/(1+math.pow(6*do_out.gamma, 2))*math.sqrt(math.pi/(3*math.radians(d_sin.delta2)))
            do_out.K17 = 1/(1+0.6*math.pow(d_sin.D/(do_out.sef), 1/3)*(d_sin.b2/d_sin.D)*math.radians(d_sin.delta2))
            do_out.sigma_mx = 4*do_out.M1/(math.pi*math.pow(d_sin.D, 2)*(do_out.sef))

            do_out.v1_2 = -0.23*do_out.K13*do_out.K15/(do_out.K12*do_out.K10)
            do_out.v1_3 = -0.53*do_out.K11/(do_out.K14*do_out.K16*do_out.K17*math.sin(0.5*math.radians(d_sin.delta2)))
            
            do_out.K2 = 1.25 # добавить для условий монтажа
            do_out.v21_2 = -do_out.sigma_mx/(do_out.K2*d_sin.sigma_d)
            do_out.v21_3 = 0
            do_out.v22_2 = ((d_sin.p*d_sin.D)/(4*(do_out.sef))-do_out.sigma_mx)/(do_out.K2*d_sin.sigma_d)
            do_out.v22_3 = ((d_sin.p*d_sin.D)/(2*(do_out.sef)))/(do_out.K2*d_sin.sigma_d)

            do_out.K1_21 = (1-math.pow(do_out.v21_2, 2))/((1/3+do_out.v1_2*do_out.v21_2)+math.sqrt(math.pow(1/3+do_out.v1_2*do_out.v21_2, 2)+(1-math.pow(do_out.v21_2, 2))*math.pow(do_out.v1_2, 2)))
            do_out.K1_22 = (1-math.pow(do_out.v22_2, 2))/((1/3+do_out.v1_2*do_out.v22_2)+math.sqrt(math.pow(1/3+do_out.v1_2*do_out.v22_2, 2)+(1-math.pow(do_out.v22_2, 2))*math.pow(do_out.v1_2, 2)))

            do_out.K1_31 = (1-math.pow(do_out.v21_3, 2))/((1/3+do_out.v1_3*do_out.v21_3)+math.sqrt(math.pow(1/3+do_out.v1_3*do_out.v21_3, 2)+(1-math.pow(do_out.v21_3, 2))*math.pow(do_out.v1_3, 2)))
            do_out.K1_32 = (1-math.pow(do_out.v22_3, 2))/((1/3+do_out.v1_3*do_out.v22_3)+math.sqrt(math.pow(1/3+do_out.v1_3*do_out.v22_3, 2)+(1-math.pow(do_out.v22_3, 2))*math.pow(do_out.v1_3, 2)))

            do_out.sigmai2_1 = do_out.K1_21*do_out.K2*d_sin.sigma_d
            do_out.sigmai2_2 = do_out.K1_22*do_out.K2*d_sin.sigma_d
            do_out.sigmai2 = min(do_out.sigmai2_1, do_out.sigmai2_2)

            do_out.sigmai3_1 = do_out.K1_31*do_out.K2*d_sin.sigma_d
            do_out.sigmai3_2 = do_out.K1_32*do_out.K2*d_sin.sigma_d
            do_out.sigmai3 = min(do_out.sigmai3_1, do_out.sigmai3_2)

            do_out.Fe = do_out.F1*(math.pi/4)*do_out.K13*do_out.K15*math.sqrt(d_sin.D/(d_sin.s-d_sin.c))

            do_out.F_d2 = 0.7*do_out.sigmai2*do_out.sef*math.sqrt(d_sin.D*do_out.sef)/(do_out.K10*do_out.K12)
            do_out.F_d3 = 0.9*do_out.sigmai3*do_out.sef*math.sqrt(d_sin.D*do_out.sef)/(do_out.K14*do_out.K16*do_out.K17)

            if d_sin.dav == 'vn':
                do_out.yslystoich2 = do_out.M1/do_out.M_d+do_out.Fe/do_out.F_d+math.pow(do_out.Q1/do_out.Q_d, 2)
            elif d_sin.dav == 'nar':
                do_out.yslystoich2 = d_sin.p/do_out.p_d+do_out.M1/do_out.M_d+do_out.Fe/do_out.F_d+math.pow(do_out.Q1/do_out.Q_d, 2)

        return do_out


    def calc_heat(self, d_in:data_heatin):
        import math
        d_out = data_heatout()
        
        if d_in.type == 'nepodviz':
            d_out.mn = d_in.a / d_in.a1
            d_out.etam = 1 - (d_in.i * (d_in.dT ** 2)) / (4 * (d_in.a1 ** 2))
            d_out.etaT = 1 - (d_in.i*((d_in.dt - 2 * d_in.sT) ** 2)) / (4 * (d_in.a1 ** 2))

            d_out.Ky = d_in.ET * (d_out.etaT - d_out.etam) / d_in.l
            d_out.ro = d_out.Ky * d_in.a1 * d_in.l / (d_in.EK * d_in.sK)

            if d_in.komp == 0: # без компенсатора
                d_out.Kqz, d_out.Kpz = 0
            elif d_in.komp == 1: # с компенсатором
                d_out.Kqz = math.pi * d_in.a * d_in.EK * d_in.sK / (d_in.l * d_in.Kkom)
                d_out.Kpz = math.pi * ((d_in.Dkom ** 2) - (d_in.dkom ** 2)) * d_in.EK * d_in.sK / (4.8 * d_in.l * d_in.a * d_in.Kkom)
            elif d_in.komp == 2: # с расширителем
                pass
            elif d_in.komp == 3: # с компенсатором на расширителе
                pass

            d_out.Kq = 1 + d_out.Kqz
            d_out.Kp = 1+ d_out.Kpz
            
            d_out.etaTr = int(d_out.etaT * 20) / 20
            if d_out.etaTr in data_fiz.eta_list:
                d_out.psi0 = data_fiz.eta_list[d_out.etaTr]
            else:
                print('Error psi0')

            if d_in.typep == 0:
                d_out.beta = (1.82 / d_in.sp) * ((d_out.Ky * d_in.sp)/(d_out.psi0 * d_in.Ep) ** .25)
            elif d_in.typep == 1:
                pass

            d_out.omega = d_out.beta * d_in.a1

            d_out.fip = 1 - d_in.d0 / d_in.tp
            
            
            d_out.b1 = (d_in.DH - d_in.D) / 2
            d_out.R1 = (d_in.DH - d_in.D) / 4
            d_out.b2 = (d_in.DH - d_in.D) / 2
            d_out.R2 = (d_in.DH - d_in.D) / 4

            d_out.beta1 = 1.3 / ((d_in.a * d_in.s1) ** .5)
            d_out.beta2 = 1.3 / ((d_in.a * d_in.s2) ** .5)
            d_out.K1 = d_out.beta1 * d_in.a * d_in.EK * (d_in.s1 ** 3) / (5.5 * d_out.R1)
            d_out.K2 = d_out.beta2 * d_in.a * d_in.ED * (d_in.s2 ** 3) / (5.5 * d_out.R2)
            d_out.Kf1 = d_in.E1 * (d_in.h1 ** 3) * d_out.b1 /(12 * (d_out.R1 ** 2)) + d_out.K1 * (1 + d_out.beta1 * d_in.h1 / 2)
            d_out.Kf2 = d_in.E2 * (d_in.h2 ** 3) * d_out.b2 /(12 * (d_out.R2 ** 2)) + d_out.K2 * (1 + d_out.beta2 * d_in.h2 / 2)
            d_out.Kf = d_out.Kf1 + d_out.Kf2

            d_out.mcp = 0.15 * d_in.i * ((d_in.dT - d_in.sT) ** 2) / (d_in.a1 ** 2)

            d_out.p0 = (d_in.alfaK * (d_in.tK - d_in.t0) - d_in.alfaT * (d_in.tT - d_in.t0)) * d_out.Ky * d_in.l + (d_out.etaT - 1 + d_out.mcp + d_out.mn * (d_out.mn + 0.5 * d_out.ro * d_out.Kq)) * d_in.pt - (d_out.etam - 1 + d_out.mcp + d_out.mn * (d_out.mn + 0.3 * d_out.ro * d_out.Kp)) * d_in.pm
        
            
        elif d_in.type == 'plav':
            
            

            if True:
                d_out.dE = d_in.d0 - 2 * d_in.sT
            else:
                d_out.dE = d_in.d0 - d_in.sT

            d_out.fiE = 1 - d_out.dE / d_in.tp



        elif d_in.type == 'U':
            pass

        
        
        