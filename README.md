# app-config

You need to define `appconfig.ini` file in your application, something like this:

    [section_name]

    # string value
    param_1=value
    
    # integer value
    param_2=11
    
    # boolean value
    param_3=1 # True values is: 1, true/True/True, yes/Yes/YES, да/Да/ДА


#### Usage:

    import appconfig
    
    # get string config value
    appconfig.get_str('section_name', 'param_1') // 'value'
    
    # get float value
    appconfig.get_float('section_name', 'param_2') // 11.0
    
    # get int value
    appconfig.get_int('section_name', 'param_2') // 11
    
    # get bool value
    appconfig.get_float('section_name', 'param_3') // True


Also, if you want to check config value on correctly, you can set `lazy` parameter to False.
For example, in this code `appconfig.get_int('section_name', 'param_1')` you get `appconfig.exceptions.BadValueException`