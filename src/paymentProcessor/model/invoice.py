from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

from paymentProcessor.model.invoice_detail import InvoiceDetail
from paymentProcessor.model.invoice_header import InvoiceHeader
from paymentProcessor.model.invoice_summary import InvoiceSummary


def to_dict(filecontent):
    invoice_detail = InvoiceDetail(filecontent)
    return {
        'Invoice_Header': InvoiceHeader(filecontent).to_dict(),
        'Invoice_Detail': invoice_detail.to_dict(),
        'Invoice_Summary': InvoiceSummary(invoice_detail.calculate_summary()).to_dict()
    }


def to_xml(filecontent):
    xml_string = parseString(dicttoxml(to_dict(filecontent), custom_root='Invoice', attr_type=False)).toxml()
    xml_string = str('<?xml version="1.0" ?><Invoice doctype="ETS Invoice" version="3.1">'
                     + xml_string.split('<?xml version="1.0" ?><Invoice>', 1)[1])
    return xml_string.replace('<item>', '').replace('</item>', '')


def to_txt(model):
    dict_model = to_dict(model)
    txt_string = '%s\n%s\n%s\n%s\n%s\n\n\n\n\n%s, den %s\t\t\t\t\t\t%s\n\t\t\t\t\t\t\t\t\t\t\t%s\n\t\t\t\t\t\t\t\t\t' \
                 '\t\t%s' \
                 % (model[1][2], model[1][3], model[1][4], model[1][5], model[1][6]
                    , model[0][2], model[0][3]
                    , model[2][2], model[2][3], model[2][4])

    txt_string += '\n\nKundennummer:\t\t %s\nAuftragsnummer:\t\t %s\n\nRechnung Nr\t\t\t%s\n-------------------------' \
                  % (model[1][1], model[0][1], model[0][0])

    for item in dict_model.get('Invoice_Detail'):
        item = item.get('Invoice_Items')
        txt_string += '\n{0:4}   Positionsbeschreibung der Pos:{0:4}\t {1:4} x {2:9.2f}  {3}\t   {4:9.2f}  {5:3.2f}%' \
            .format(int(item.get('I.D.010_Basisdaten').get('BV.010_Positions_Nr_in_der_Rechnung'))
                    , int(item.get('I.D.020_Preise_und_Mengen').get('BV.010_Verrechnete_Menge'))
                    , float(item.get('I.D.020_Preise_und_Mengen').get('BV.030_Verrechneter_Einzelpreis_des_Artikels'))
                    , item.get('I.D.020_Preise_und_Mengen').get('BV.040_Waehrung_des_Einzelpreises')
                    , float(
                item.get('I.D.020_Preise_und_Mengen').get('BV.070_Bestaetigter_Gesamtpreis_der_Position_netto'))
                    , float(item.get('I.D.030_Steuern').get('BV.030_Steuersatz')))

    txt_string += '\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  --------------'

    txt_string += '\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t Total {0}\t   {1:9.2f}\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t MWST  {2}\t   {3:9.2f}' \
        .format(dict_model.get('Invoice_Summary').get('I.S.010_Basisdaten').get(
        'BV.030_Waehrung_Gesamtbetrag_der_Rechnung_exkl_MwSt_exkl_Ab_Zuschlag')
                , float(dict_model.get('Invoice_Summary').get('I.S.010_Basisdaten').get(
            'BV.020_Gesamtbetrag_der_Rechnung_exkl_MwSt_exkl_Ab_Zuschlag'))
                , dict_model.get('Invoice_Summary').get('I.S.020_Aufschluesselung_der_Steuern').get(
            'BV.055_Waehrung_Steuerbetrag')
                , float(dict_model.get('Invoice_Summary').get('I.S.020_Aufschluesselung_der_Steuern').get(
            'BV.050_Steuerbetrag')))

    date_string = dict_model.get('Invoice_Header').get('I.H.080_Zahlungsbedingungen').get('BV.020_Zahlungsbedingungen_Zusatzwert')
    txt_string += '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nZahlungsziel ohne Abzug{0:3} Tage ({1})\n\nEinzahlungsschein' \
        .format(int(model[0][5]), '{0}.{1}.{2}'.format(date_string[6:8], date_string[4:6], date_string[0:4]))

    txt_string += '\n\n\n\n\n\n\n\n\n\n\n\n\t{0} . {1}\t\t\t\t\t{0} . {1}\t\t{2}\n\t\t\t\t\t\t\t\t\t\t\t\t{3}\n0 00000 00000 00000\t\t\t\t\t\t\t\t{4}'\
        .format(dict_model.get('Invoice_Summary').get('I.S.010_Basisdaten').get(
            'BV.020_Gesamtbetrag_der_Rechnung_exkl_MwSt_exkl_Ab_Zuschlag').split('.')[0]
        , str(dict_model.get('Invoice_Summary').get('I.S.010_Basisdaten').get(
            'BV.020_Gesamtbetrag_der_Rechnung_exkl_MwSt_exkl_Ab_Zuschlag')).split('.')[1]
        , model[2][2], model[2][3], model[2][4])

    txt_string += f'\n\n{model[2][2]}\n{model[2][3]}\n{model[2][4]}'

    return txt_string
