import chainermn


def main():
    comm = chainermn.create_communicator("hierarchical")
    print(f"hi from {comm.rank}")


if __name__ == "__main__":
    main()
