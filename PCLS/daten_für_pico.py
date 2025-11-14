# ssd1306.py – MicroPython library for 128x32 / 128x64 OLED displays via I2C
# Compatible with SSD1306 controller

import framebuf

class SSD1306:
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.width * self.pages)
        self.framebuf = framebuf.FrameBuffer(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.poweron()
        self.init_display()

    def init_display(self):
        for cmd in (
            0xae, 0xd5, 0x80, 0xa8, self.height - 1, 0xd3, 0x00, 0x40, 0x8d,
            0x10 if self.external_vcc else 0x14, 0x20, 0x00, 0xa1, 0xc8, 0xda,
            0x02 if self.height == 32 else 0x12, 0x81, 0x8f, 0xd9,
            0x22 if self.external_vcc else 0xf1, 0xdb, 0x40, 0xa4, 0xa6, 0xaf):
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def poweroff(self):
        self.write_cmd(0xae)

    def poweron(self):
        self.write_cmd(0xaf)

    def contrast(self, contrast):
        self.write_cmd(0x81)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(0xa7 if invert else 0xa6)

    def show(self):
        for page in range(self.pages):
            self.write_cmd(0xb0 | page)
            self.write_cmd(0x00)
            self.write_cmd(0x10)
            self.write_data(self.buffer[self.width * page:self.width * (page + 1)])

class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3c, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.temp[0] = 0x80
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, buf):
        self.i2c.writeto(self.addr, b'\x40' + buf)
