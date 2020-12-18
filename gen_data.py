import random
from faker import Faker
from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFont
# pictures number
num_pics = 20
# language
fake = Faker('ja_JP')

# position
name_title_pos = (42,45)
add_title_pos = (42,140)
is_title_pos = (42,185)
cons_title_pos = (42, 296)
ib_title_pos = (49,380)
r_number_title_pos = [(27,455), (27,495), (39,535), (27, 569)]
name_pos = (106,40)
dob_pos = (630,45)
address_pos = (112,135)
doi_pos = (140,180)
dov_pos = (20,223)
con_1_pos = (156,291)
con_2_pos = (156,315)
con_3_pos = (156, 345)
l1_pos = (95,438)
l2_pos = (539,436)
number_pos = (161,438)
random_number_pos = [(83,490), (83,527), (83, 562)]
horizon_letters_pos = [(632,256), (632,300), (632,350), (632,402), (632,450)]
type_pos = [(364,509), (364, 557)]
authority_pos = (724,531)
authority1_pos = (694,567)
line1_pos_pos = [(395,500), (428,500), (463,500), (495,500), (527,500), (561,500), (594,500)]
line1_neg_pos = [(395,500), (428,500), (460,500), (493,500), (527,500), (558,500), (589,500)]
line2_pos_pos = [(395,555), (428,555), (463,555), (495,555), (527,555), (561,555), (594,555)]
line2_neg_pos = [(395,560), (428,560), (460,560), (493,560), (527,560), (558,560), (594,560)]

# range data
years_dob = range(50, 99)
months = range(1,13)
days = range(1,32)
year_issue = range(1, 20)
year_valid = range(00,99)

# load image
image = Image.open('demo.jpg')

# load fonts
font_name = ImageFont.truetype('fonts/Kosugi-Regular.ttf', 40)
font_title = ImageFont.truetype('fonts/KosugiMaru-Regular.ttf', 25)
font_dob = ImageFont.truetype('fonts/KosugiMaru-Regular.ttf', 33)
font_doi = ImageFont.truetype('fonts/KosugiMaru-Regular.ttf', 38)
font_valid = ImageFont.truetype('fonts/Kosugi-Regular.ttf', 50)
font_cons = ImageFont.truetype('fonts/Kosugi-Regular.ttf',23)
font_number_license = ImageFont.truetype('fonts/OCRB Medium.ttf', 40)
font_r_number = ImageFont.truetype('fonts/KosugiMaru-Regular.ttf',30)
font_authority = ImageFont.truetype('fonts/KosugiMaru-Regular.ttf',20)


def random_number(list_range):
    return str(random.choice(list_range))


def gen_data():
    for num_pic in tqdm(range(num_pics)):
        s1 = fake.sentence()[:2]
        s2 = fake.sentence()[:3]
        s3 = fake.sentence()[:5]
        s4 = fake.sentence()[:8]
        conditions = ["", s1, s2, s3, s4]
        authority = '{}'.format(fake.sentence()[:3])
        authority1 = '{}'.format(fake.sentence()[:5])
        img = image.copy()
        draw = ImageDraw.Draw(img)
        # random data
        name_title = fake.sentence()[:2]
        name = fake.name()
        name = "   ".join(name)
        y = random_number(years_dob)
        m = random_number(months)
        d = random_number(days)
        dob = fake.sentence()[:2] + y + fake.sentence()[:1] + " " + m + fake.sentence()[:1] + " " + d + fake.sentence()[:2]
        add_title = fake.sentence()[:2]
        address = fake.address()[: random.randrange(20, 23)]
        is_title = fake.sentence()[:2]
        y_issue = random_number(year_issue)
        m_issue = random_number((months))
        d_issue = random_number(days)
        if len(y_issue) < 2:
            y_issue = y_issue.zfill(2)
        if len(m_issue) < 2:
             m_issue = m_issue.zfill(2)
        if len(d_issue) < 2:
            d_issue = d_issue.zfill(2)
        r_number = str(random.randint(0, 99999)).zfill(5)
        # date of issue
        doi = fake.sentence()[:2] + y_issue + fake.sentence()[:1] + " " + m_issue + fake.sentence()[:1] +" " + d_issue + fake.sentence()[:1] + "   " + r_number
        y_vaild = random_number(year_valid).zfill(2)
        m_vaild = random_number(months).zfill(2)
        d_valid = random_number(days).zfill(2)
        dov = fake.sentence()[:2] + y_vaild + fake.sentence()[:1] + m_vaild + fake.sentence()[:1] + d_valid + fake.sentence()[:5]
        cons_title = fake.sentence()[:2]
        # random 1,2,3 in coditions. Some has 1, some has 2, some has 3
        cons1 = random.choice(conditions[1:])
        conditions.remove(cons1)
        cons2 = random.choice(conditions)
        if cons2 != "":
            conditions.remove(cons2)
            cons3 = random.choice(conditions)
        else:
            cons3 = ""
        ib_title = fake.sentence()[:2]
        number_license = random_number(range(0, 999999999999)).zfill(12)
        l1 = fake.sentence()[:1]
        l2 = fake.sentence()[:1]
        # draw & write to labels
        with open('labels/{}.gt'.format(num_pic), 'w', encoding='utf8') as f:
            with open('labels/{}.jpg.txt'.format(num_pic), 'w', encoding='utf8') as f1:
                draw.text(name_title_pos, name_title, font=font_title, fill=(50, 50, 50))
                size = font_title.getsize(name_title)
                xmin = str(name_title_pos[0])
                ymin = str(name_title_pos[1])
                xmax = str(name_title_pos[0] + size[0])
                ymax = str(name_title_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin,ymin, xmax,ymin,xmax,ymax,xmin,ymax, name_title))
                f1.write(
                    '{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, name_title))
                draw.text(name_pos, name, font=font_name, fill=(50,50,50))
                size = font_name.getsize(name)
                xmin = str(name_pos[0])
                ymin = str(name_pos[1])
                xmax = str(name_pos[0] + size[0])
                ymax = str(name_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin,ymin, xmax,ymin,xmax,ymax,xmin,ymax, "".join(name.split())))
                f1.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax,
                                                              "".join(name.split())))
                draw.text(dob_pos, dob, font=font_dob, fill=(0,0,0))
                size = font_dob.getsize(dob)
                xmin = str(dob_pos[0])
                ymin = str(dob_pos[1])
                xmax = str(dob_pos[0] + size[0])
                ymax = str(dob_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin,ymin, xmax,ymin,xmax,ymax,xmin,ymax,"".join(dob.split())))
                f1.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax,
                                                              "".join(dob.split())))
                draw.text(add_title_pos, add_title, font=font_title, fill=(50, 50, 50))
                size = font_title.getsize(add_title)
                xmin = str(add_title_pos[0])
                ymin = str(add_title_pos[1])
                xmax = str(add_title_pos[0] + size[0])
                ymax = str(add_title_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax,add_title))
                f1.write(
                    '{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, add_title))
                draw.text(address_pos, address, font=font_name, fill=(0,0,0))
                size = font_name.getsize(address)
                xmin = str(address_pos[0])
                ymin = str(address_pos[1])
                xmax = str(address_pos[0] + size[0])
                ymax = str(address_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, address))
                f1.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, address))

                draw.text(is_title_pos, is_title, font=font_title, fill=(50, 50, 50))
                size = font_title.getsize(is_title)
                xmin = str(is_title_pos[0])
                ymin = str(is_title_pos[1])
                xmax = str(is_title_pos[0] + size[0])
                ymax = str(is_title_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, is_title))
                f1.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, is_title))

                draw.text(doi_pos, doi, font=font_doi, fill=(0,12,29))
                size = font_doi.getsize(doi)
                xmin = str(doi_pos[0])
                ymin = str(doi_pos[1])
                xmax = str(doi_pos[0] + size[0])
                ymax = str(doi_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, "".join(doi.split())))
                f1.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax,
                                                              "".join(doi.split())))

                draw.text(dov_pos, dov, font=font_valid, fill=(5,16,28))
                size = font_valid.getsize(dov)
                xmin = str(dov_pos[0])
                ymin = str(dov_pos[1])
                xmax = str(dov_pos[0] + size[0])
                ymax = str(dov_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, dov))
                f1.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, dov))

                draw.text(cons_title_pos, cons_title, font=font_title, fill=(5, 16, 28))
                size = font_title.getsize(cons_title)
                xmin = str(cons_title_pos[0])
                ymin = str(cons_title_pos[1])
                xmax = str(cons_title_pos[0] + size[0])
                ymax = str(cons_title_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, cons_title))
                f1.write(
                    '{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, cons_title))

                draw.text(con_1_pos, cons1, font=font_cons, fill=(30,30,30))
                size = font_cons.getsize(cons1)
                xmin = str(con_1_pos[0])
                ymin = str(con_1_pos[1])
                xmax = str(con_1_pos[0] + size[0])
                ymax = str(con_1_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, cons1))
                f1.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, cons1))
                if cons2 != "":
                    draw.text(con_2_pos, cons2, font=font_cons, fill=(30,30,30))
                    size = font_cons.getsize(cons2)
                    xmin = str(con_2_pos[0])
                    ymin = str(con_2_pos[1])
                    xmax = str(con_2_pos[0] + size[0])
                    ymax = str(con_2_pos[1] + size[1])
                    f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, cons2))
                    f1.write(
                        '{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, cons2))

                if cons3 != "":
                    draw.text(con_3_pos, cons3, font=font_cons, fill=(30, 30, 30))
                    size = font_cons.getsize(cons3)
                    xmin = str(con_3_pos[0])
                    ymin = str(con_3_pos[1])
                    xmax = str(con_3_pos[0] + size[0])
                    ymax = str(con_3_pos[1] + size[1])
                    f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, cons3))
                    f1.write(
                        '{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, cons3))

                draw.text(ib_title_pos, ib_title, font=font_dob, fill=(5, 16, 28))
                size = font_dob.getsize(ib_title)
                xmin = str(ib_title_pos[0])
                ymin = str(ib_title_pos[1])
                xmax = str(ib_title_pos[0] + size[0])
                ymax = str(ib_title_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, ib_title))
                f1.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, ib_title))

                draw.text(number_pos, number_license, font=font_number_license, fill=(30,30,30))
                draw.text(l1_pos, l1, font=font_doi, fill=(30, 30, 30))
                draw.text(l2_pos, l2, font=font_doi, fill=(30, 30, 30))
                size = font_doi.getsize(l2)
                xmin = str(l1_pos[0])
                ymin = str(l1_pos[1])
                xmax = str(l2_pos[0] + size[0])
                ymax = str(l2_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, l1 + number_license + l2))
                f1.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax,
                                                              l1 + number_license + l2))
                draw.text(authority_pos, authority, font=font_authority, fill=(200,73,40))
                draw.text(authority1_pos, authority1, font=font_authority, fill=(200, 73, 40))
                size = font_authority.getsize(authority1)
                xmin = str(authority1_pos[0])
                ymin = str(authority_pos[1])
                xmax = str(authority1_pos[0] + size[0])
                ymax = str(authority1_pos[1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, authority + authority1))
                f1.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax,
                                                              authority + authority1))

                for i in r_number_title_pos:
                    title = fake.sentence()[:random.randrange(1,3)]
                    if i ==  (39,535):
                        title = fake.sentence()[:1]
                    draw.text(i, title, font=font_title, fill=(0, 0, 0))
                    size = font_title.getsize(title)
                    xmin = str(i[0])
                    ymin = str(i[1])
                    xmax = str(i[0] + size[0])
                    ymax = str(i[1] + size[1])
                    f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, title))
                    f1.write(
                        '{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, title))
                for i in random_number_pos:
                    n = fake.sentence()[:2 ] + random_number(range(0,99)).zfill(2) +" "+ fake.sentence()[:1] +  random_number(range(0,99)).zfill(2) + fake.sentence()[:1] + " " + random_number(range(0,99)).zfill(2) +  fake.sentence()[:1]
                    draw.text(i, n, font = font_r_number, fill=(0,0,0))
                    size = font_r_number.getsize(n)
                    xmin = str(i[0])
                    ymin = str(i[1])
                    xmax = str(i[0] + size[0])
                    ymax = str(i[1] + size[1])
                    f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, n))
                    f1.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, n))

                ho_str = ""
                for i in horizon_letters_pos:
                    letter = fake.word()[:1]
                    ho_str += letter
                    draw.text(i, letter, font=font_dob, fill=(50, 167, 202))
                    if i == horizon_letters_pos[-1]:
                        size = font_dob.getsize(letter)
                xmin = str(horizon_letters_pos[0][0])
                ymin = str(horizon_letters_pos[0][1])
                xmax = str(horizon_letters_pos[-1][0] + size[0])
                ymax = str(horizon_letters_pos[-1][1] + size[1])
                f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, ho_str))
                f1.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, ho_str))

                for i in type_pos:
                    letter = fake.word()[:1]
                    draw.text(i, letter, font=font_title, fill=(30, 30, 30))
                    size = font_title.getsize(letter)
                    xmin = str(i[0])
                    ymin = str(i[1])
                    xmax = str(i[0] + size[0])
                    ymax = str(i[1] + size[1])
                    f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, letter))
                    f1.write(
                        '{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, letter))

                line1_pos = int(random_number(range(0,7)))
                line2_pos = int(random_number(range(0,7)))

                for i in range(7):
                    if i == line1_pos:
                        t = fake.word()[:1]
                        draw.text(line1_pos_pos[i], t, font=font_title, fill=(30,30,30))
                        size = font_title.getsize(t)
                        xmin = str(line1_pos_pos[i][0])
                        ymin = str(line1_pos_pos[i][1])
                        xmax = str(line1_pos_pos[i][0] + size[0])
                        ymax = str(line1_pos_pos[i][1] + size[1])
                        f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, t))
                        f1.write(
                            '{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, t))
                    else:
                        draw.text(line1_neg_pos[i], '-', font=font_number_license, fill=(30, 30, 30))

                for i in range(7):
                    if i == line2_pos:
                        t = fake.word()[:1]
                        draw.text(line2_pos_pos[i], t, font=font_title, fill=(30,30,30))
                        size = font_title.getsize(t)
                        xmin = str(line2_pos_pos[i][0])
                        ymin = str(line2_pos_pos[i][1])
                        xmax = str(line2_pos_pos[i][0] + size[0])
                        ymax = str(line2_pos_pos[i][1] + size[1])
                        f.write('{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, t))
                        f1.write(
                            '{},{},{},{},{},{},{},{},{}\n'.format(xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax, t))
                    else:
                        draw.text(line2_neg_pos[i], '-', font=font_number_license, fill=(30, 30, 30))
        img.save('images/{}.jpg'.format(num_pic))


def main():
    gen_data()


if __name__ =='__main__':
    main()
