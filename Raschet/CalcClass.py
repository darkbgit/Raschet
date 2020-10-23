


class data_in(object):
    name = str()
    steel = str()
    press = float()
    temp = int()
    sigma_d = float()
    dia = int()
    c_kor = float()
    c_minus = float()
    c_3=float()
    fi = float()
    s_prin = float()
    dav = str('vn')
    l = float()
    l3_1 = float(0)
    l3_2 = float(0)
    E = int()
    ny = float(2.4)
    met = str()

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
    R=float()
    err = str()

class CalcClass(object):
    """description of class"""

    import json
    import data_fiz

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
        if name in self.data_fiz.E_list.keys():
            for t in self.data_fiz.E_list[name]:
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
                    #sigma_str = str(sigma).split('.')
                    #if sigma_str[1] > '5':
                    #    sigma_str[1] = '5'
                    #    sigma = float('.'.join(sigma_str))
                    #elif sigma_str[1] < '5':
                    #    sigma_str[1] = '0'
                    #    sigma = float('.'.join(sigma_str))
                
                    break
            return E
        else:
            return f'Сталь {name} не найдена'



    def calc_ob(self, data_in:data_in): #sigma_d, press, dia, c_kor, c_minus, fi, s_prin=0.0, dav='vn', l=0, E=0):
        import math
        """ 
        in data_in(name, steel, press, temp, sigma_d, 
            dia, c_kor, c_minus, fi, s_prin,
            dav - 'vn' or 'nar'
            l=0 ,l3_1=0, l3_2=0 E=0)
          out data_out [0] - s_calcr [1] - s_calc [2] - s_prin [3] - press_d [4] - c
        """
        do_out = data_out()
        if data_in.dav == 'vn':
            do_out.s_calcr = data_in.press * data_in.dia / ((2 * data_in.sigma_d * data_in.fi) - data_in.press)
            do_out.c = data_in.c_kor + data_in.c_minus
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
            do_out.c = data_in.c_kor + data_in.c_minus
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

