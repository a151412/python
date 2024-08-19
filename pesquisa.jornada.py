import win32evtlog
import win32evtlogutil
import win32con
from datetime import datetime, timedelta

# Definir o nome do log e os identificadores de evento
log_name = 'Security'
logon_event_id = 4624
logoff_event_id = 4634

# Abrir o log de eventos
handle = win32evtlog.OpenEventLog(None, log_name)

# Configurar o arquivo de saída
with open("eventos_logon_logoff.txt", "w") as file:
    flags = win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total_records = win32evtlog.GetNumberOfEventLogRecords(handle)
    events = []
    logon_times = []
    logoff_times = []

    while True:
        records = win32evtlog.ReadEventLog(handle, flags, 0)
        if not records:
            break
        for event in records:
            event_time = event.TimeGenerated.Format()
            event_time = datetime.strptime(event_time, '%a %b %d %H:%M:%S %Y')
            if event.EventID == logon_event_id:
                logon_times.append(event_time)
                file.write(f"Logon: {event_time}\n")
            elif event.EventID == logoff_event_id:
                logoff_times.append(event_time)
                file.write(f"Logoff: {event_time}\n")

    # Ordenar as listas para garantir que estejam em ordem cronológica
    logon_times.sort()
    logoff_times.sort()

    # Calcular o tempo total de sessão
    total_session_time = timedelta()
    for logon_time in logon_times:
        logoff_time = next((l for l in logoff_times if l > logon_time), None)
        if logoff_time:
            session_time = logoff_time - logon_time
            total_session_time += session_time
            file.write(f"Período de sessão: {session_time} (de {logon_time} até {logoff_time})\n")

    file.write(f"\nTempo total de sessão: {total_session_time}\n")

win32evtlog.CloseEventLog(handle)
print("Eventos salvos em 'eventos_logon_logoff.txt'.")
