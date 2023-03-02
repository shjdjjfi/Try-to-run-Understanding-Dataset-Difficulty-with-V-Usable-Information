import augment

if __name__ == "__main__":
    augment.SNLIStandardTransformation('./data').transform()
    augment.SNLINullTransformation('./data').transform()

