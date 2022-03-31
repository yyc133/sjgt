# -*- coding: utf-8 -*-


import re

def extract_gsbh(text):
    hz = re.findall(r'(?<![0-9])([G|S][0-9]{1,4})(?![0-9])', text)
    if hz:
        hz = hz[0]
        start = text.find(hz)
        end = start + len(hz)
        return hz, start, end
    else:
        return '', -1, -1

def extract_gszh(text):
    hz = re.findall(r'(?<![0-9])([K][0-9+-]{1,9})(?![0-9])', text)
    if hz:
        hz = hz[0]
        start = text.find(hz)
        end = start + len(hz)
        return hz, start, end
    else:
        return '', -1, -1

def person_elements(regex, text):
    re_element = re.search(regex, text)
    if re_element:
        return re_element.groupdict()['item'], re_element.start(), re_element.end()
    else:
        return '', -1, -1 


def get_basic_info_gsbh(text):

    basic_info_gsbh, _min, _max = person_elements(
        regex=r'(?P<item>[GS][0-9]+)(?:.{2,8}高速)(?:.{2,5}段)?(?:K[0-9]+(\+[0-9]+)?)?',
        text=text
    )

    if not basic_info_gsbh:
        basic_info_hz, _min, _max = extract_gsbh(text)

    return basic_info_gsbh, _min, _max


def get_basic_info_gszh(text):

    basic_info_gszh, _min, _max = person_elements(
        regex=r'(?:[GS][0-9]+)(?:.{2,8}高速)(?:.{2,5}段)?(?P<item>K[0-9]+(\+[0-9]+)?)?',
        text=text
    )

    if not basic_info_gszh:
        basic_info_hz, _min, _max = extract_gszh(text)

    return basic_info_gszh, _min, _max


def get_basic_info_gsmc(text):

    basic_info_gsmc, _min, _max = person_elements(
        regex=r'(?:[GS][0-9]+)(?P<item>.{2,8}高速)(?:.{2,5}段)?(?:K[0-9]+(\+[0-9]+)?)?',
        text=text
    )

    return basic_info_gsmc, _min, _max



def get_basic_info_gsld(text):

    basic_info_gsld, _min, _max = person_elements(
        regex=r'(?:[GS][0-9]+)(?:.{2,8}高速)(?P<item>.{2,5}段)?(?:K[0-9]+(\+[0-9]+)?)?',
        text=text
    )

    if not basic_info_gsld:
        basic_info_gsld, _min, _max = person_elements(
        regex=r'高速(?P<item>[^，,、。:：]*?)段',
        text=text
    )
    basic_info_gsld = basic_info_gsld + "段"

    return basic_info_gsld, _min, _max



def get_basic_info_gs(text):

    basic_info_gs, _min, _max = person_elements(
        regex=r'(?P<item>高速)',
        text=text
    )

    if not basic_info_gs:
        basic_info_gs = "市内"

    return basic_info_gs, _min, _max


def get_basic_info_sj(text):
    
    basic_info_sj, _min, _max = person_elements(
        regex=r'(?P<item>解除|解封|恢复通行)',
        text=text
    )

    if basic_info_sj:
        basic_info_sj = "解除"
        
    else :
        basic_info_sj = "发出"

    return basic_info_sj, _min, _max



if __name__ == '__main__':
    content = "G75兰海高速崇遵段K1169+600处发生交通事故，目前交警在K1178处交通管制，预计3小时恢复通行。"
    print(get_basic_info_gsmc(content))
