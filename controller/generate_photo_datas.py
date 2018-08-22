from models.generate_data import generate, save_numpy_data


def main():
    classes = ["monkey", "boar", "crow"]
    image_size = 50
    save_dir = './photos.npy'

    data = generate(classes, image_size)
    save_numpy_data(data, save_dir)


if __name__ == '__main__':
    main()