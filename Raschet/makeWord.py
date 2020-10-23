import CalcClass
import docx
import decimal


def makeWord_obvn(data_in:CalcClass.data_in, data_out:CalcClass.data_out, docum=None):
    doc = docx.Document(docum)
    doc.add_heading(f'Расчет на прочность обечайки {data_in.name}, нагруженной внутренним избыточным давлением').paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph('').paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph('Исходные данные').paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table = doc.add_table(rows=0, cols=0)
    table.add_column(7000000)
    table.add_column(750000) #.alignment = docx.enum.table.WD_TABLE_ALIGNMENT.CENTER
    table.add_column(750000)
    table.add_row()  
    table.cell(0, 0).text = 'Наименование и размерность'
    table.cell(0, 0).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(0, 1).text = 'Обозначение'
    table.cell(0, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(0, 2).text = 'Значение'
    table.add_row()
    table.cell(1, 0).text = 'Расчетная температура, °С'
    table.cell(1, 1).text = 't'
    table.cell(1, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(1, 2).text = f'{data_in.temp}'
    table.add_row()
    table.cell(2, 0).text = 'Расчетное внутреннее давление, МПа'
    table.cell(2, 1).text ='p'
    table.cell(2, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(2, 2).text =f'{data_in.press}'
    table.add_row()
    table.cell(3, 0).text = 'Марка стали'
    table.cell(3, 1).text =''
    table.cell(3, 2).text =f'{data_in.steel}'
    table.add_row()
    table.cell(4, 0).text = 'Допускаемое напряжение при расчетной температуре, МПа'
    table.cell(4, 1).text = '[σ]'
    table.cell(4, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(4, 2).text =f'{data_in.sigma_d}'
    table.add_row()
    table.cell(5, 0).text = 'Коэффициент прочности сварного шва'
    table.cell(5, 1).paragraphs[0].add_run('φ_p').font.math = True
    #table.cell(5, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(5, 2).text =f'{data_in.fi}'
    table.add_row()
    table.cell(6, 0).text = 'Внутренний диаметр аппарата, мм'
    table.cell(6, 1).text = 'D'
    table.cell(6, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(6, 2).text =f'{data_in.dia}'
    table.add_row()
    table.cell(7, 0).text = 'Прибавка на коррозию, мм'
    table.cell(7, 1).paragraphs[0].add_run('c_1').font.math = True
    #table.cell(7, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(7, 2).text =f'{data_in.c_kor}'
    table.add_row()
    table.cell(8, 0).text = 'Прибавка для компенсации минусового допуска листа, мм'
    table.cell(8, 1).paragraphs[0].add_run('c_2').font.math = True
    #table.cell(8, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(8, 2).text =f'{data_in.c_minus}'
    doc.add_paragraph('')
    doc.add_paragraph('Результаты расчета').paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph('')
    doc.add_paragraph('Толщину стенки вычисляют по формуле:')
    doc.add_paragraph().add_run('s≥s_p+c').font.math = True
    p = doc.add_paragraph('где ')
    p.add_run('s_p').font.math = True
    p.add_run(' - расчетная толщина стенки обечайки')
    doc.add_paragraph().add_run('s_p=(p∙D)/(2∙[σ]∙φ_p-p)').font.math = True
    doc.add_paragraph('c - сумма прибавок к расчетной толщине')
    doc.add_paragraph().add_run('c=c_1+c_2').font.math = True
    doc.add_paragraph().add_run(f'c={data_in.c_kor}+{data_in.c_minus}={data_out.c:.2f} мм').font.math = True
    doc.add_paragraph().add_run(f's_p=({data_in.press}∙{data_in.dia})/(2∙{data_in.sigma_d}∙{data_in.fi}-{data_in.press})={data_out.s_calcr:.2f} мм').font.math = True
    doc.add_paragraph().add_run(f's={data_out.s_calcr:.2f}+{data_out.c:.2f}={data_out.s_calc:.2f} мм').font.math = True
    if data_in.s_prin > data_out.s_calc:
        doc.add_paragraph(f'Принятая толщина s={data_in.s_prin} мм')
    else:
        doc.add_paragraph().add_run(f'Принятая толщина s={data_in.s_prin} мм').font.color.rgb = docx.shared.RGBColor(255,0,0)
    doc.add_paragraph('Допускаемое внутреннее избыточное давление вычисляют по формуле:')
    doc.add_paragraph().add_run('[p]=(2∙[σ]∙φ_p∙(s-c))/(D+s-c)').font.math = True
    doc.add_paragraph().add_run(f'[p]=(2∙{data_in.sigma_d}∙{data_in.fi}∙({data_in.s_prin}-{data_out.c:.2f}))/({data_in.dia}+{data_in.s_prin}-{data_out.c:.2f})={data_out.press_d:.2f} МПа').font.math = True
    doc.add_paragraph().add_run('[p]≥p').font.math = True
    doc.add_paragraph().add_run(f'{data_out.press_d:.2f}≥{data_in.press}').font.math = True
    if data_out.press_d > data_in.press:
        doc.add_paragraph('Условие прочности выполняется')
    else:
        doc.add_paragraph().add_run('Условие прочности не выполняется').font.color.rgb = docx.shared.RGBColor(255,0,0)
    p = doc.add_paragraph('Границы применения формул ')
    if data_in.dia >= 200:
        p.add_run('при D ≥ 200 мм')
        doc.add_paragraph().add_run('(s-c)/(D)≤0.1').font.math = True
        doc.add_paragraph().add_run(f'({data_in.s_prin}-{data_out.c:.2f})/({data_in.dia})={(data_in.s_prin-data_out.c)/data_in.dia:.3f}≤0.1').font.math = True
    else:
        p.add_run('при D < 200 мм')
        doc.add_paragraph().add_run('(s-c)/(D)≤0.3').font.math = True
        doc.add_paragraph().add_run(f'({data_in.s_prin}-{data_out.c:.2f})/({data_in.dia})={(data_in.s_prin-data_out.c)/data_in.dia:.2f}≤0.3').font.math = True

    doc.save(docum)


def makeWord_obnar(data_in:CalcClass.data_in, data_out:CalcClass.data_out, docum=None):
    doc = docx.Document(docum)
    doc.add_heading(f'Расчет на прочность обечайки {data_in.name}, нагруженной наружным давлением').paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph('').paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph('Исходные данные').paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table = doc.add_table(rows=0, cols=0)
    table.add_column(7000000)
    table.add_column(750000) #.alignment = docx.enum.table.WD_TABLE_ALIGNMENT.CENTER
    table.add_column(750000)
    table.add_row()  
    table.cell(0, 0).text = 'Наименование и размерность'
    table.cell(0, 0).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(0, 1).text = 'Обозначение'
    table.cell(0, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(0, 2).text = 'Значение'
    table.add_row()
    table.cell(1, 0).text = 'Расчетная температура, °С'
    table.cell(1, 1).text = 't'
    table.cell(1, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(1, 2).text = f'{data_in.temp}'
    table.add_row()
    table.cell(2, 0).text = 'Расчетное внутреннее давление, МПа'
    table.cell(2, 1).text ='p'
    table.cell(2, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(2, 2).text =f'{data_in.press}'
    table.add_row()
    table.cell(3, 0).text = 'Марка стали'
    table.cell(3, 1).text =''
    table.cell(3, 2).text =f'{data_in.steel}'
    table.add_row()
    table.cell(4, 0).text = 'Допускаемое напряжение при расчетной температуре, МПа'
    table.cell(4, 1).text = '[σ]'
    table.cell(4, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(4, 2).text =f'{data_in.sigma_d}'
    table.add_row()
    table.cell(5, 0).text = 'Модуль продольной упругости при расчетной темп-ре, МПа'
    table.cell(5, 1).text = 'E'
    table.cell(5, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(5, 2).text =f'{data_in.E}'
    table.add_row()
    table.cell(6, 0).text = 'Коэффициент прочности сварного шва'
    table.cell(6, 1).paragraphs[0].add_run('φ_p').font.math = True
    #table.cell(6, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(6, 2).text =f'{data_in.fi}'
    table.add_row()
    table.cell(7, 0).text = 'Внутренний диаметр аппарата, мм'
    table.cell(7, 1).text = 'D'
    table.cell(7, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(7, 2).text =f'{data_in.dia}'
    table.add_row()
    table.cell(8, 0).text = 'Длина обечайки, мм'
    table.cell(8, 1).text = 'l'
    table.cell(8, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(8, 2).text =f'{data_in.l}'
    table.add_row()
    table.cell(9, 0).text = 'Прибавка на коррозию, мм'
    table.cell(9, 1).paragraphs[0].add_run('c_1').font.math = True
    #table.cell(9, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(9, 2).text =f'{data_in.c_kor}'
    table.add_row()
    table.cell(10, 0).text = 'Прибавка для компенсации минусового допуска листа, мм'
    table.cell(10, 1).paragraphs[0].add_run('c_2').font.math = True
    #table.cell(10, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(10, 2).text =f'{data_in.c_minus}'
    doc.add_paragraph('')
    doc.add_paragraph('Результаты расчета').paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph('')
    doc.add_paragraph('Толщину стенки вычисляют по формуле:')
    doc.add_paragraph().add_run('s≥s_p+c').font.math = True
    p = doc.add_paragraph('где ')
    p.add_run('s_p').font.math = True
    p.add_run(' - расчетная толщина стенки обечайки')
    doc.add_paragraph().add_run('s_p=max{1.06∙(10^-2∙D)/(B)∙(p/(10^-5∙E)∙l/D)^0.4;(1.2∙p∙D)/(2∙[σ]-p)}').font.math = True
    doc.add_paragraph('Коэффициент B вычисляют по формуле:')
    doc.add_paragraph().add_run('B=max{1;0.47∙(p/(10^-5∙E))^0.067∙(l/D)^0.4}').font.math = True
    doc.add_paragraph().add_run(f'0.47∙({data_in.press}/(10^-5∙{data_in.E}))^0.067∙({data_out.l}/{data_in.dia})^0.4={data_out.b_2:.2f}').font.math = True
    doc.add_paragraph().add_run(f'B=max(1;{data_out.b_2:.2f})={data_out.b:.2f}').font.math = True
    doc.add_paragraph('c - сумма прибавок к расчетной толщине')
    doc.add_paragraph().add_run('c=c_1+c_2').font.math = True
    doc.add_paragraph().add_run(f'c={data_in.c_kor}+{data_in.c_minus}={data_out.c:.2f} мм').font.math = True
    
    doc.add_paragraph().add_run(f'1.06∙(10^-2∙{data_in.dia})/({data_out.b:.2f})∙({data_in.press}/(10^-5∙{data_in.E})∙{data_out.l}/{data_in.dia})^0.4={data_out.s_calcr1:.2f}').font.math = True
    doc.add_paragraph().add_run(f'(1.2∙{data_in.press}∙{data_in.dia})/(2∙{data_in.sigma_d}-{data_in.press})={data_out.s_calcr2:.2f}').font.math = True
    doc.add_paragraph().add_run(f's_p=max({data_out.s_calcr1:.2f};{data_out.s_calcr2:.2f})={data_out.s_calcr:.2f} мм').font.math = True

    doc.add_paragraph().add_run(f's={data_out.s_calcr:.2f}+{data_out.c:.2f}={data_out.s_calc:.2f} мм').font.math = True
    if data_in.s_prin > data_out.s_calc:
        doc.add_paragraph(f'Принятая толщина s={data_in.s_prin} мм')
    else:
        doc.add_paragraph().add_run(f'Принятая толщина s={data_in.s_prin} мм').font.color.rgb = docx.shared.RGBColor(255,0,0)
    doc.add_paragraph('Допускаемое наружное давление вычисляют по формуле:')
    doc.add_paragraph().add_run('[p]=[p]_П/√(1+([p]_П/[p]_E)^2)').font.math = True
    doc.add_paragraph('допускаемое давление из условия прочности вычисляют по формуле:')
    doc.add_paragraph().add_run('[p]_П=(2∙[σ]∙(s-c))/(D+s-c)').font.math = True
    doc.add_paragraph().add_run(f'[p]_П=(2∙{data_in.sigma_d}∙({data_in.s_prin}-{data_out.c:.2f}))/({data_in.dia}+{data_in.s_prin}-{data_out.c:.2f})={data_out.press_dp:.2f} МПа').font.math = True
    doc.add_paragraph('допускаемое давление из условия устойчивости в пределах упругости вычисляют по формуле:')
    doc.add_paragraph().add_run('[p]_E=(2.08∙10^-5∙E)/(n_y∙B_1)∙D/l∙[(100∙(s-c))/D]^2.5').font.math = True
    p = doc.add_paragraph('коэффициент ')
    p.add_run('B_1').font.math = True
    p.add_run(' вычисляют по формуле')
    doc.add_paragraph().add_run('B_1=min{1;9.45∙D/l∙√(D/(100∙(s-c)))}').font.math = True
    doc.add_paragraph().add_run(f'9.45∙{data_in.dia}/{data_out.l}∙√({data_in.dia}/(100∙({data_in.s_prin}-{data_out.c:.2f})))={data_out.b1_2:.2f}').font.math = True
    doc.add_paragraph().add_run(f'B_1=min(1;{data_out.b1_2:.2f})={data_out.b1:.1f}').font.math = True
    doc.add_paragraph().add_run(f'[p]_E=(2.08∙10^-5∙{data_in.E})/({data_in.ny}∙{data_out.b1:.1f})∙{data_in.dia}/{data_out.l}∙[(100∙({data_in.s_prin}-{data_out.c:.2f}))/{data_in.dia}]^2.5={data_out.press_de:.2f} МПа').font.math = True
    doc.add_paragraph().add_run(f'[p]={data_out.press_dp:.2f}/√(1+({data_out.press_dp:.2f}/{data_out.press_de:.2f})^2)={data_out.press_d:.2f} МПа').font.math = True
    doc.add_paragraph().add_run('[p]≥p').font.math = True
    doc.add_paragraph().add_run(f'{data_out.press_d:.2f}≥{data_in.press}').font.math = True
    if data_out.press_d > data_in.press:
        doc.add_paragraph('Условие прочности выполняется')
    else:
        doc.add_paragraph().add_run('Условие прочности не выполняется').font.color.rgb = docx.shared.RGBColor(255,0,0)
    p = doc.add_paragraph('Границы применения формул ')
    if data_in.dia >= 200:
        p.add_run('при D ≥ 200 мм')
        doc.add_paragraph().add_run('(s-c)/(D)≤0.1').font.math = True
        doc.add_paragraph().add_run(f'({data_in.s_prin}-{data_out.c:.2f})/({data_in.dia})={(data_in.s_prin-data_out.c)/data_in.dia:.3f}≤0.1').font.math = True
    else:
        p.add_run('при D < 200 мм')
        doc.add_paragraph().add_run('(s-c)/(D)≤0.3').font.math = True
        doc.add_paragraph().add_run(f'({data_in.s_prin}-{data_out.c:.2f})/({data_in.dia})={(data_in.s_prin-data_out.c)/data_in.dia:.2f}≤0.3').font.math = True

    doc.save(docum)


def makeWord_elvn(data_in:CalcClass.data_in, data_out:CalcClass_datadata_out, docum=None):

    doc = docx.Document(docum)
    doc.add_heading(f'Расчет на прочность эллептического днища {data_in.name}, нагруженного внутренним избыточным давлением').paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph('').paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph('Исходные данные').paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table = doc.add_table(rows=0, cols=0)
    table.add_column(7000000)
    table.add_column(750000) #.alignment = docx.enum.table.WD_TABLE_ALIGNMENT.CENTER
    table.add_column(750000)
    table.add_row()  
    table.cell(0, 0).text = 'Наименование и размерность'
    table.cell(0, 0).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(0, 1).text = 'Обозначение'
    table.cell(0, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(0, 2).text = 'Значение'
    table.add_row()
    table.cell(1, 0).text = 'Расчетная температура, °С'
    table.cell(1, 1).text = 't'
    table.cell(1, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(1, 2).text = f'{data_in.temp}'
    table.add_row()
    table.cell(2, 0).text = 'Расчетное внутреннее давление, МПа'
    table.cell(2, 1).text ='p'
    table.cell(2, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(2, 2).text =f'{data_in.press}'
    table.add_row()
    table.cell(3, 0).text = 'Марка стали'
    table.cell(3, 1).text =''
    table.cell(3, 2).text =f'{data_in.steel}'
    table.add_row()
    table.cell(4, 0).text = 'Допускаемое напряжение при расчетной температуре, МПа'
    table.cell(4, 1).text = '[σ]'
    table.cell(4, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(4, 2).text =f'{data_in.sigma_d}'
    table.add_row()
    table.cell(5, 0).text = 'Коэффициент прочности сварного шва'
    table.cell(5, 1).paragraphs[0].add_run('φ_p').font.math = True
    #table.cell(5, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(5, 2).text =f'{data_in.fi}'
    table.add_row()
    table.cell(6, 0).text = 'Внутренний диаметр аппарата, мм'
    table.cell(6, 1).text = 'D'
    table.cell(6, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(6, 2).text =f'{data_in.dia}'
    table.add_row()
    table.cell(7, 0).text = 'Прибавка на коррозию, мм'
    table.cell(7, 1).paragraphs[0].add_run('c_1').font.math = True
    #table.cell(7, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(7, 2).text =f'{data_in.c_kor}'
    table.add_row()
    table.cell(8, 0).text = 'Прибавка для компенсации минусового допуска листа, мм'
    table.cell(8, 1).paragraphs[0].add_run('c_2').font.math = True
    #table.cell(8, 1).paragraphs[0].paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    table.cell(8, 2).text =f'{data_in.c_minus}'
    doc.add_paragraph('')
    doc.add_paragraph('Результаты расчета').paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph('')
    doc.add_paragraph('Толщину стенки вычисляют по формуле:')
    doc.add_paragraph().add_run('s_1≥s_1p+c').font.math = True
    p = doc.add_paragraph('где ')
    p.add_run('s_1p').font.math = True
    p.add_run(' - расчетная толщина стенки обечайки')
    doc.add_paragraph().add_run('s_1p=(p∙R)/(2∙[σ]∙φ-0.5∙p)').font.math = True
    doc.add_paragraph('где R - радиус кривизны в вершине днища')
    doc.add_paragraph('R=D={data_in.dia} мм - для эллиптичекских днищ с H=0.25D')
    doc.add_paragraph('c - сумма прибавок к расчетной толщине')
    doc.add_paragraph().add_run('c=c_1+c_2').font.math = True
    doc.add_paragraph().add_run(f'c={data_in.c_kor}+{data_in.c_minus}={data_out.c:.2f} мм').font.math = True
    doc.add_paragraph().add_run(f's_p=({data_in.press}∙{data_out.R})/(2∙{data_in.sigma_d}∙{data_in.fi}-0.5{data_in.press})={data_out.s_calcr:.2f} мм').font.math = True
    doc.add_paragraph().add_run(f's={data_out.s_calcr:.2f}+{data_out.c:.2f}={data_out.s_calc:.2f} мм').font.math = True
    if data_in.s_prin > data_out.s_calc:
        doc.add_paragraph(f'Принятая толщина s={data_in.s_prin} мм')
    else:
        doc.add_paragraph().add_run(f'Принятая толщина s={data_in.s_prin} мм').font.color.rgb = docx.shared.RGBColor(255,0,0)
    doc.add_paragraph('Допускаемое внутреннее избыточное давление вычисляют по формуле:')
    doc.add_paragraph().add_run('[p]=(2∙[σ]∙φ_p∙(s-c))/(D+s-c)').font.math = True
    doc.add_paragraph().add_run(f'[p]=(2∙{data_in.sigma_d}∙{data_in.fi}∙({data_in.s_prin}-{data_out.c:.2f}))/({data_in.dia}+{data_in.s_prin}-{data_out.c:.2f})={data_out.press_d:.2f} МПа').font.math = True
    doc.add_paragraph().add_run('[p]≥p').font.math = True
    doc.add_paragraph().add_run(f'{data_out.press_d:.2f}≥{data_in.press}').font.math = True
    if data_out.press_d > data_in.press:
        doc.add_paragraph('Условие прочности выполняется')
    else:
        doc.add_paragraph().add_run('Условие прочности не выполняется').font.color.rgb = docx.shared.RGBColor(255,0,0)
    p = doc.add_paragraph('Границы применения формул ')
    if data_in.dia >= 200:
        p.add_run('при D ≥ 200 мм')
        doc.add_paragraph().add_run('(s-c)/(D)≤0.1').font.math = True
        doc.add_paragraph().add_run(f'({data_in.s_prin}-{data_out.c:.2f})/({data_in.dia})={(data_in.s_prin-data_out.c)/data_in.dia:.3f}≤0.1').font.math = True
    else:
        p.add_run('при D < 200 мм')
        doc.add_paragraph().add_run('(s-c)/(D)≤0.3').font.math = True
        doc.add_paragraph().add_run(f'({data_in.s_prin}-{data_out.c:.2f})/({data_in.dia})={(data_in.s_prin-data_out.c)/data_in.dia:.2f}≤0.3').font.math = True

    doc.save(docum)


