# (id, name, url)
endpoints = {
    '1': ('A,C,E','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace'),
    '2': ('B,D,F,M','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm'),
    '3': ('G','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g'),
    '4': ('J,Z','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz'),
    '5': ('N,Q,R,W','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw'),
    '6': ('L','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l'),
    '7': ('1,2,3,4,5,6','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs'),
    '8': ('7','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-7'),
    '9': ('SIR','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-si'),
    '10': ('Elevator/Escalator Listing','http://advisory.mtanyct.info/eedevwebsvc/allequipments.aspx'),
    '11': ('Elevator/Escalator Status','http://web.mta.info/developers/data/nyct/nyct_ene.xml'),
    '12': ('Service Status Combined','http://web.mta.info/status/serviceStatus.txt'),
    '13': ('Service Status-Individual Subway Lines','http://web.mta.info/status/ServiceStatusSubway.xml'),
    '14': ('Service Status - Bus','http://web.mta.info/status/ServiceStatusBus.xml'),
    '15': ('Planned Work','http://web.mta.info/developers/data/nyct/plannedwork.xml'),
    '16': ('Lost and Found Data','http://advisory.mtanyct.info/LPUWebServices/CurrentLostProperty.aspx'),
    '17': ('Long Island Rail Road','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/lirr%2Fgtfs-lirr'),
    '18': ('Metro-North Railroad','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/mnr%2Fgtfs-mnr'),
    '19': ('All Service Alerts','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fall-alerts'),
    '20': ('Subway Alerts','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fsubway-alerts'),
    '21': ('Bus Alerts','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fbus-alerts'),
    '22': ('Long Island Rail Road Alerts','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Flirr-alerts'),
    '23': ('Metro-North Railroad Alerts','https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fmnr-alerts')
}

id_name_listing = '\n'.join([ k +' : '+v[0] for k,v in endpoints.items()])