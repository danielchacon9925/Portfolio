#include "psp_api.h"
#include "bsp_external_interrupts.h"
#include "psp_ext_interrupts_eh1.h"
#include "bsp_timer.h"
#include "bsp_printf.h"

#define SegEn_ADDR      0x80001038
#define SegDig_ADDR     0x8000103C

#define GPIO_SWs        0x80001400
#define GPIO_LEDs       0x80001404
#define GPIO_INOUT      0x80001408
#define RGPIO_INTE      0x8000140C
#define RGPIO_PTRIG     0x80001410
#define RGPIO_CTRL      0x80001418
#define RGPIO_INTS      0x8000141C

#define RPTC_CNTR       0x80001200
#define RPTC_HRC        0x80001204
#define RPTC_LRC        0x80001208
#define RPTC_CTRL       0x8000120c

#define Select_INT      0x80001018

int SegDisplCount=0;

extern D_PSP_DATA_SECTION D_PSP_ALIGNED(1024) pspInterruptHandler_t G_Ext_Interrupt_Handlers[8];


void GPIO_ISR(void)
{
  unsigned int i;

  /* Write the LED */
  i = M_PSP_READ_REGISTER_32(GPIO_LEDs);             /* RGPIO_OUT */
  i = !i;                                            /* Invert the LEDs */
  i = i & 0x1;                                       /* Keep only the right-most LED */
  M_PSP_WRITE_REGISTER_32(GPIO_LEDs, i);             /* RGPIO_OUT */

  /* Clear GPIO interrupt */
  M_PSP_WRITE_REGISTER_32(RGPIO_INTS, 0x0);           /* RGPIO_INTS */

  /* Stop the generation of the specific external interrupt */
  bspClearExtInterrupt(4);
}


void DefaultInitialization(void)
{
  u32_t uiSourceId;

  /* Register interrupt vector */
  pspInterruptsSetVectorTableAddress(&M_PSP_VECT_TABLE);

  /* Set external-interrupts vector-table address in MEIVT CSR */
  pspExternalInterruptSetVectorTableAddress(G_Ext_Interrupt_Handlers);

  /* Put the Generation-Register in its initial state (no external interrupts are generated) */
  bspInitializeGenerationRegister(D_PSP_EXT_INT_ACTIVE_HIGH);

  for (uiSourceId = D_BSP_FIRST_IRQ_NUM; uiSourceId <= D_BSP_LAST_IRQ_NUM; uiSourceId++)
  {
    /* Make sure the external-interrupt triggers are cleared */
    bspClearExtInterrupt(uiSourceId);
  }

  /* Set Standard priority order */
  pspExtInterruptSetPriorityOrder(D_PSP_EXT_INT_STANDARD_PRIORITY);

  /* Set interrupts threshold to minimal (== all interrupts should be served) */
  pspExtInterruptsSetThreshold(M_PSP_EXT_INT_THRESHOLD_UNMASK_ALL_VALUE);

  /* Set the nesting priority threshold to minimal (== all interrupts should be served) */
  pspExtInterruptsSetNestingPriorityThreshold(M_PSP_EXT_INT_THRESHOLD_UNMASK_ALL_VALUE);
}


void ExternalIntLine_Initialization(u32_t uiSourceId, u32_t priority, pspInterruptHandler_t pTestIsr)
{
  /* Set Gateway Interrupt type (Level) */
  pspExtInterruptSetType(uiSourceId, D_PSP_EXT_INT_LEVEL_TRIG_TYPE);

  /* Set gateway Polarity (Active high) */
  pspExtInterruptSetPolarity(uiSourceId, D_PSP_EXT_INT_ACTIVE_HIGH);

  /* Clear the gateway */
  pspExtInterruptClearPendingInt(uiSourceId);

  /* Set IRQ4 priority */
  pspExtInterruptSetPriority(uiSourceId, priority);
    
  /* Enable IRQ4 interrupts in the PIC */
  pspExternalInterruptEnableNumber(uiSourceId);

  /* Register ISR */
  G_Ext_Interrupt_Handlers[uiSourceId] = pTestIsr;
}


void GPIO_Initialization(void)
{
  /* Configure LEDs and Switches */
  M_PSP_WRITE_REGISTER_32(GPIO_INOUT, 0xFFFF);        /* GPIO_INOUT */
  M_PSP_WRITE_REGISTER_32(GPIO_LEDs, 0x0);            /* GPIO_LEDs */

  /* Configure GPIO interrupts */
  M_PSP_WRITE_REGISTER_32(RGPIO_INTE, 0x10000);       /* RGPIO_INTE */
  M_PSP_WRITE_REGISTER_32(RGPIO_PTRIG, 0x10000);      /* RGPIO_PTRIG */
  M_PSP_WRITE_REGISTER_32(RGPIO_INTS, 0x0);           /* RGPIO_INTS */
  M_PSP_WRITE_REGISTER_32(RGPIO_CTRL, 0x1);           /* RGPIO_CTRL */
}


int main(void)
{
  int count=0, i;

  /* INITIALIZE THE INTERRUPT SYSTEM */
  DefaultInitialization();                            /* Default initialization */
  pspExtInterruptsSetThreshold(5);                    /* Set interrupts threshold to 5 */

  /* INITIALIZE INTERRUPT LINE IRQ4 */
  ExternalIntLine_Initialization(4, 6, GPIO_ISR);     /* Initialize line IRQ4 with a priority of 6. Set GPIO_ISR as the Interrupt Service Routine */
  M_PSP_WRITE_REGISTER_32(Select_INT, 0x1);           /* Connect the GPIO interrupt to the IRQ4 interrupt line */

  /* INITIALIZE THE PERIPHERALS */
  GPIO_Initialization();                              /* Initialize the GPIO */
  M_PSP_WRITE_REGISTER_32(SegEn_ADDR, 0x0);           /* Initialize the 7-Seg Displays */

  /* ENABLE INTERRUPTS */
  pspInterruptsEnable();                              /* Enable all interrupts in mstatus CSR */
  M_PSP_SET_CSR(D_PSP_MIE_NUM, D_PSP_MIE_MEIE_MASK);  /* Enable external interrupts in mie CSR */

  while (1) {
    /* Increase 7-Seg Displays */
    M_PSP_WRITE_REGISTER_32(SegDig_ADDR, count);
    count++;

    /* Delay */
    for(i=0;i<50000000;i++);
  }
}

