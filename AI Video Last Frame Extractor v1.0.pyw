import pygame
import av
import sys
from datetime import datetime
from PIL import Image

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("AI Video Last Frame Extractor v1.0")

screen.fill((80, 80, 80))
pygame.display.flip()


def save_last_frame(video_path):

    print("Feldolgozás:", video_path)

    container = av.open(video_path)
    stream = container.streams.video[0]

    if container.duration:
        container.seek(container.duration, any_frame=False, backward=True)

    frame = None

    for packet in container.demux(stream):
        for f in packet.decode():
            frame = f

    if frame is None:
        print("Nem találtam frame-et.")
        return

    img = frame.to_ndarray(format="rgb24")

    filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"

    image = Image.fromarray(img)
    image.save(filename, "JPEG")

    print("Mentve:", filename)


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.DROPFILE:

            video_file = event.file

            save_last_frame(video_file)