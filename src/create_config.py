import json

data = {}
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
