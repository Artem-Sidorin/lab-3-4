warning = 'Значения суммы, срока и процентной ставки не может быть меньше 0'


def annuity(period, percent):
    try:
        n = period * 12
        m = percent / 100 / 12
        an_ratio = m / (1 - (1 + m) ** (-n))
    except ZeroDivisionError:
        an_ratio = 0
    return an_ratio


def diff(summ, period, percent):
    try:
        m_payment = []
        mp_cnt = period * 12
        rest = summ
        mp_real = summ / (period * 12.0)
    except ZeroDivisionError:
        mp_real = 0
    while mp_cnt != 0:
        mp = mp_real + (rest * percent / 1200)
        m_payment.append(round(mp, 2))
        rest = rest - mp_real
        mp_cnt = mp_cnt - 1
    return m_payment


def ann_result(summ, period, percent):
    if (summ or period or percent) < 0:
        return warning, warning, warning
    else:
        m_payment = summ * annuity(period, percent)
        deb_perc = m_payment * period * 12 - summ
        total = m_payment * period * 12
        return m_payment, deb_perc, total


def diff_result(summ, period, percent):
    if (summ or period or percent) < 0:
        return warning, warning, warning
    else:
        m_payment = diff(summ, period, percent)
        total = round(sum(m_payment), 2)
        deb_perc = total - summ
        return m_payment, deb_perc, total
