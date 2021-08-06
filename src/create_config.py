import json

data = {}
data['mic'] = []
data['mic'].append({
    'type': 'None Respeaker Mic',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False            
})
data['mic'].append({
    'type': 'ReSpeaker 2-Mics Pi HAT',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker 4-Mics Pi HAT',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker Mic Array v2.0',
    'led_off_mode': 1,
    'led_off_color': 0xFFFF99,
    'led_wakeup_mode': 2,
    'led_wakeup_color': 0x33FFFF,    
    'is_active': True        
})
data['mic'].append({
    'type': 'ReSpeaker Core v2.0',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['volume'] = []
data['volume'].append({
    'value': 50,
    'type': 'event'    
})
data['volume'].append({
    'value': 50,
    'type': 'speak'    
})
data['volume'].append({
    'value': 50,
    'type': 'playback'    
})
data['tts_engine'] = []
data['tts_engine'].append({
    'token': '',
    'token_file': '',        
    'name': 'tts_gg_free',
    'voice_name': '',    
    'speed': '',
    'pitch': '',
    'is_active': False    
})
data['tts_engine'].append({
    'token': 'AIzaSw6_k16b3c',
    'token_file': 'google.json',    
    'name': 'tts_gg_cloud',    
    'voice_name': 'vi-VN-Wavenet-A',
    'speed': 1.0,
    'pitch': 0,
    'is_active': True    
})
data['tts_engine'].append({
    'token': 'SythBY7N8AUXxzdWRNwYE8N',
    'token_file': '',    
    'name': 'tts_viettel',    
    'voice_name': 'hcm-diemmy2',
    'speed': 1.0,
    'pitch': '',
    'is_active': False    
})
data['tts_engine'].append({
    'token': '8sJJ39XC2fRGU',
    'token_file': '',    
    'name': 'tts_zalo',
    'voice_name': '1',    
    'speed': 1.0,
    'pitch': '',
    'is_active': False    
})    
data['tts_engine'].append({
    'token': '7591A4mt9NkyEqEC',
    'name': 'tts_fpt',
    'voice_name': 'linhsan',
    'speed': 1.0,
    'pitch': '',    
    'is_active': False    
})
with open('config.json', 'w') as outfile:
    json.dump(data, outfile)
