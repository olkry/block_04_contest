from random import choice


class MarsURLEncoder:

    def __init__(self):
        self.link_dict = {}
        self.avail_val = ([chr(ch) for ch in range(ord('a'), ord('z') + 1)] +
                          [chr(ch) for ch in range(ord('A'), ord('Z') + 1)] +
                          [str(ch) for ch in range(10)])

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        encode_str = ''
        while not encode_str or encode_str in self.link_dict:
            for _ in range(6):
                encode_str += choice(self.avail_val)
        enc_str = 'https://ma.rs/' + encode_str
        self.link_dict[enc_str] = long_url
        return enc_str

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.link_dict[short_url]


if __name__ == '__main__':
    selamel = MarsURLEncoder()
    selamel.encode('https://ma.rs/45346/659/X7NYIol')
    selamel.encode('https://ma.rs/X7435Iol/dfgh/5576')
    selamel.encode('https://ma.rs/4456/hg/X6456YIol')
    selamel.encode('https://ma.rs/sde45/567/X7rtuIol')
    selamel.encode('https://ma.rs/ert/456/X7ghjIol')
    selamel.encode('https://ma.rs/9554/dfg/X7kjhgIol')
    print(selamel.link_dict)
    short_u = list(selamel.link_dict.keys())
    print(short_u[1])
    print(short_u[3])
    print(short_u[5])
    print(selamel.decode(short_u[1]))
    print(selamel.decode(short_u[3]))
    print(selamel.decode(short_u[5]))
