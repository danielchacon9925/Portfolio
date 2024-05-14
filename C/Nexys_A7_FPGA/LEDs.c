// Mem directions
#define RPTC_HRC_R 0x80001244
#define RPTC_LRC_R 0x80001248
#define RPTC_CTRL_R 0x8000124C
#define RPTC_HRC_G 0x80001284
#define RPTC_LRC_G 0x80001288
#define RPTC_CTRL_G 0x8000128C
#define RPTC_HRC_B 0x800012C4
#define RPTC_LRC_B 0x800012C8
#define RPTC_CTRL_B 0x800012CC

// Switches
#define GPIO_SWs 0x80001400
// GPIO
#define GPIO_INOUT 0x80001408

#define READ(dir) (*(volatile char *)dir)

#define WRITE(dir, value)                  \
    {                                      \
        (*(volatile char *)dir) = (value); \
    }

int main(void)
{
    WRITE(GPIO_INOUT, 0xFFFF);

    // Restart counter
    WRITE(RPTC_CTRL_R, 0x80);
    WRITE(RPTC_CTRL_G, 0x80);
    WRITE(RPTC_CTRL_B, 0x80);

    // MAX Value
    WRITE(RPTC_LRC_R, 0xFFFFE);
    WRITE(RPTC_LRC_G, 0xFFFFE);
    WRITE(RPTC_LRC_B, 0xFFFFE);

    // PWM Enable
    WRITE(RPTC_CTRL_R, 0X1);
    WRITE(RPTC_CTRL_G, 0X1);
    WRITE(RPTC_CTRL_B, 0X1);

    int switches_value;

    while (1)
    {

        switches_value = READ(GPIO_SWs);
        switches_value = (switches_value >> 16);
        // Set value
        WRITE(RPTC_HRC_R, 1048574 - ((switches_value & 0b11111) * 8322));
        WRITE(RPTC_HRC_G, 1048574 - (((switches_value >> 5) & 0b11111) * 8322));
        WRITE(RPTC_HRC_B, 1048574 - (((switches_value >> 10) & 0b11111) * 8322));
    }
    return 0;
}