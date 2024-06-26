import math
import os
import PIL.Image as Image


# Environment variables
elite_repositories = os.environ['ELITE_CODE_REPOSITORIES']
library_repository = os.environ['ELITE_LIBRARY_REPOSITORY']
aviator_repository = os.environ['AVIATOR_CODE_REPOSITORY']
revs_repository = os.environ['REVS_CODE_REPOSITORY']
lander_repository = os.environ['LANDER_CODE_REPOSITORY']


def generate_image(source_files, image_name):

    data_block = bytearray()

    for file in source_files:
        elite_file = open(file, "rb")
        data_block.extend(elite_file.read())
        elite_file.close()

    image_width = math.ceil(math.sqrt(len(data_block)))
    image_size = image_width * image_width

    print("\nGenerating image: {}".format(image_name))
    print("Code size: {}".format(len(data_block)))
    print("Image size: {0} x {0}".format(image_width))

    if len(data_block) < image_size:
        need_bytes = image_size - len(data_block)
        data_block.extend([0] * need_bytes)

    image = Image.frombytes("L", (image_width, image_width), bytes(data_block), "raw")

    image.save(image_name)


image_name = "cassette.png"
source_files = [
    elite_repositories + "/cassette-elite-beebasm/3-assembled-output/ELITE.bin",
    elite_repositories + "/cassette-elite-beebasm/3-assembled-output/ELTcode.bin"
]
generate_image(source_files, image_name)

image_name = "disc.png"
source_files = [
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/ELITE2.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/ELITE3.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/ELITE4.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/T.CODE.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.CODE.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOA.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOB.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOC.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOD.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOE.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOF.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOG.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOH.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOI.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOJ.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOK.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOL.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOM.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MON.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOO.bin",
    elite_repositories + "/disc-elite-beebasm/3-assembled-output/D.MOP.bin"
]
generate_image(source_files, image_name)

image_name = "electron.png"
source_files = [
    elite_repositories + "/electron-elite-beebasm/3-assembled-output/ELITEDA.bin",
    elite_repositories + "/electron-elite-beebasm/3-assembled-output/ELITECO.bin"
]
generate_image(source_files, image_name)

image_name = "6502sp.png"
source_files = [
    elite_repositories + "/6502sp-elite-beebasm/3-assembled-output/ELITE.bin",
    elite_repositories + "/6502sp-elite-beebasm/3-assembled-output/ELITEa.bin",
    elite_repositories + "/6502sp-elite-beebasm/3-assembled-output/I.CODE.bin",
    elite_repositories + "/6502sp-elite-beebasm/3-assembled-output/P.CODE.bin"
]
generate_image(source_files, image_name)

image_name = "master.png"
source_files = [
    elite_repositories + "/master-elite-beebasm/3-assembled-output/M128Elt.bin",
    elite_repositories + "/master-elite-beebasm/3-assembled-output/BCODE.bin",
    elite_repositories + "/master-elite-beebasm/3-assembled-output/BDATA.bin"
]
generate_image(source_files, image_name)

image_name = "nes.png"
source_files = [
    elite_repositories + "/nes-elite-beebasm/3-assembled-output/elite.bin"
]
generate_image(source_files, image_name)

image_name = "elite-a.png"
source_files = [
    elite_repositories + "/elite-a-beebasm/3-assembled-output/ELITE.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/1.D.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/1.E.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/1.F.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.A.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.B.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.C.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.D.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.E.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.F.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.G.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.H.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.I.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.J.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.K.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.L.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.M.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.N.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.O.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.P.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.Q.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.R.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.S.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.T.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.U.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.V.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/S.W.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/2.H.bin",
    elite_repositories + "/elite-a-beebasm/3-assembled-output/2.T.bin"
]
generate_image(source_files, image_name)

image_name = "revs.png"
source_files = [
    revs_repository + "/3-assembled-output/Revs2.bin",
    revs_repository + "/3-assembled-output/Silverstone.bin"
]
generate_image(source_files, image_name)

image_name = "aviator.png"
source_files = [
    aviator_repository + "/3-assembled-output/AVIA.bin"
]
generate_image(source_files, image_name)

image_name = "lander.png"
source_files = [
    lander_repository + "/3-assembled-output/GameCode.bin"
]
generate_image(source_files, image_name)
