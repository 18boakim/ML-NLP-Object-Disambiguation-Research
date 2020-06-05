import csv

with open('positions.csv', 'w') as positions:
    writer = csv.writer(positions, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(
        ['Scene ID', 'Scene Scale (Eye-to-ObjsMid Dist)', 'RO Size (edge length)', 'RO1_origin_x', 'RO1_origin_y',
         'RO1_origin_z', 'RO1_cent_x', 'RO1_cent_y', 'RO1_cent_z', 'RO2_origin_x', 'RO2_origin_y', 'RO2_origin_z',
         'RO2_cent_x', 'RO2_cent_y', 'RO2_cent_z', 'TO_origin_x', 'TO_origin_y', 'TO_origin_z', 'TO_cent_x',
         'TO_cent_y', 'TO_cent_z'])

    # ro1, ro2 = Reference Object 1, 2
    # to = Target Object
    xRangeInit = -15
    xRangeFinal = 15 + 1
    xIncrement = 10
    yRangeInit = 3
    yRangeFinal = 15 + 1
    yIncrement = 4
    zRangeInit = 15
    zRangeFinal = 45 + 1
    zIncrement = 10

    i = 0
    line = list(range(21))
    doc = []
    for sceneScale in range(1):
        for sideLength in range(1):
            for RO1x in range(3):
                for RO1y in range(3):
                    for RO1z in range(3):
                        for RO2x in range(3):
                            for RO2y in range(3):
                                for RO2z in range(3):
                                    if RO1x != RO2x or RO1y != RO2y or RO1z != RO2z:
                                        for TO1x in range(3):
                                            for TO1y in range(3):
                                                for TO1z in range(3):
                                                    if (TO1x != RO2x or TO1y != RO2y or TO1z != RO2z) and (
                                                            TO1x != RO1x or TO1y != RO1y or TO1z != RO1z):
                                                        line[0] = i
                                                        line[1] = 30
                                                        line[2] = 2
                                                        line[6] = RO1x * \
                                                            12 - 15
                                                        line[7] = RO1y * 6 + 3
                                                        line[8] = RO1z * \
                                                            15 + 15
                                                        line[3] = line[6] - 1
                                                        line[4] = line[7] - 1
                                                        line[5] = line[8] - 1
                                                        line[12] = RO2x * \
                                                            12 - 15
                                                        line[13] = RO2y * 6 + 3
                                                        line[14] = RO2z * \
                                                            15 + 15
                                                        line[9] = line[12] - 1
                                                        line[10] = line[13] - 1
                                                        line[11] = line[14] - 1
                                                        line[18] = TO1x * \
                                                            12 + 15
                                                        line[19] = TO1y * 6 + 3
                                                        line[20] = TO1z * \
                                                            15 + 15
                                                        line[15] = line[18] - .5
                                                        line[16] = line[19] - .5
                                                        line[17] = line[20] - .5
                                                        if not [line[1], line[2], line[9], line[10], line[11], line[12],
                                                                line[13], line[14], line[3], line[4], line[5], line[6],
                                                                line[7], line[8], line[15], line[16], line[17],
                                                                line[18], line[19], line[20]] in doc:
                                                            i = i + 1
                                                            print(i)
                                                            print(line)
                                                            writer.writerow(
                                                                line)
                                                            doc.append(
                                                                line[1:21])
    print(i)
