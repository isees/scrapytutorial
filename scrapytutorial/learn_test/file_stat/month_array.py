import datetime
from dateutil.relativedelta import relativedelta


def get_and_print_month_array(start_time_YYYYmm, month_range):
    start_month = datetime.datetime.strptime(start_time_YYYYmm, '%Y%m')
    m_array = []
    month_str = ''
    for i in range(month_range):
        current_month = start_month + relativedelta(months=i)
        month_str += current_month.strftime('%Y%m') + '\t'
        m_array.append(current_month.strftime('%Y%m'))
    print month_str
    return m_array
