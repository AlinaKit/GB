import json
import csv


def csv_to_json(from_csv, to_json, timed_csv, code_code):
    with (
        open(from_csv, 'r', newline='', encoding=code_code) as readed,
        open(to_json, 'w', newline='', encoding=code_code) as writed,
        open(timed_csv, 'w', newline='', encoding=code_code) as timed
    ):
        reading = csv.reader(readed, delimiter=';')
        timing = csv.writer(timed, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        all_data = []
        tim_names = []
        for i, line in enumerate(reading):
            if line[0] != '':  # повод для прерывания - первый пустой показатель первого столбца
                if i == 0:
                    # timing.writerow(line)
                    leng = len(line)
                    for j in range(0, leng):
                        tim_names.append(line[j])
                    tim_names.append('id')
                else:
                    for j in range(0, leng):
                        if line[j].isnumeric():
                            line[j] = int(line[j])
                        elif line[j] == '':
                                line[j] = None
                        else:
                            if line[j].find(','):
                                tst = line[j].replace(',', '', 1)
                            if tst.isnumeric():
                                line[j] = line[j].replace(',', '.')
                                line[j] = float(line[j])
                all_data.append(line)
        timing.writerows(all_data)
        all_data = {}
        timed.close()
        with open(timed_csv, 'r', newline='', encoding=code_code) as t_r:
            tim_dict = csv.DictReader(t_r, fieldnames=tim_names, delimiter=';')
            for i, line in enumerate(tim_dict):
                if i == 0:
                    writed.write('[')
                else:
                    line['id'] = i  # пока id равен номеру строки
                    for k in tim_names:
                        kk = {}
                        kkk = line.pop(k)
                        if isinstance(kkk, str):
                            if kkk.find('.'):
                                tst = kkk.replace('.', '', 1)
                            if kkk.isnumeric():
                                kkk = int(kkk)
                            elif tst.isnumeric():
                                kkk = float(kkk)
                        kk.setdefault(k, kkk)
                        all_data.update(kk)
                        # writed.write('\n')
                        # if k == tim_names[-1]:
                        #     writed.write('}')
                        # else:
                        #     writed.write(',\n')
                    json.dump(all_data, writed)
                    writed.write(',')
                writed.write('\n')
            json.dump({}, writed)
            writed.write(']')
                # all_data[0] = i
                # print(all_data)
            # hey = json.dumps(tim_dict, indent=4, separators=(', ', ': '))
            # json.dump(hey, writed)
