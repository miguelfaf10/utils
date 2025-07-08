import numpy as np

def mosfet_losses(parameters):

    Qg = parameters['Qg']
    Vcc = parameters['Vcc']
    Vin = parameters['Vin']
    fsw = parameters['fsw']
    I_rms = parameters['I_rms']
    Rds_on = parameters['Rds_on']
    Coss = parameters['Coss']
    t_TR = parameters['t_TR']      # t_TR : sum of the switch node transition times ON->OFF and OFF->ON
    
    # Gate Driver Losses
    Pdrv = 2*Qg*Vcc*fsw
    # FET Conduction Losses
    Pcond = 2*(I_rms**2 * Rds_on)
    # FET Switching Losses
    Pswitch = Vin*I_rms*t_TR*fsw + (Vin**2)*Coss*fsw

    print(f'Power losses:')
    print(f' - Gate Driving:   {Pdrv:.2f} W')
    print(f' - FET Conduction: {Pcond:.2f} W')
    print(f' - FET Switching:  {Pswitch:.2f} W')

    return Pdrv, Pcond, Pswitch


def classB_consumption(t_firepulse, V_firepulse, Vcc, Cload):

    I_firepulse = Cload*np.diff(V_firepulse)/np.diff(t_firepulse)
    I_firepulse_nmos = (I_firepulse + np.abs(I_firepulse))/2
    I_firepulse_pmos = (I_firepulse - np.abs(I_firepulse))/2
    
    P_nmos = (0 - V_firepulse[:-1]) * I_firepulse_nmos
    P_pmos = (Vcc - V_firepulse[:-1]) * I_firepulse_pmos

    return I_firepulse, I_firepulse_nmos, I_firepulse_pmos, P_nmos, P_pmos