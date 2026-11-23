import asyncio, json
import app

async def check_all():
    with open('token_cache.json', 'r') as f:
        cache = json.load(f)
    
    print('Testing live login status for each account...')
    results = {}
    for uid, data in cache.items():
        pw = data.get('auth_password')
        nick = data.get('nickname', 'Unknown')
        if not pw:
            print(f"{uid}: No auth_password")
            continue
        try:
            vc = await app.version_config()
            rel, cv, su = vc
            tg = await app.get_access_token(uid, pw)
            if not tg:
                print(f"{uid} ({nick}): get_access_token FAILED")
                results[uid] = {'status': 'FAILED_ACCESS_TOKEN', 'nick': nick}
                continue
            oid, at, pf = tg
            dev = app.get_device_for_account(uid)
            lpd = await app.build_majorlogin_payload(oid, at, pf, cv, dev)
            
            url = f"{su}MajorLogin" if su.endswith('/') else f"{su}/MajorLogin"
            hdrs = app.headers.copy()
            hdrs['ReleaseVersion'] = str(rel)
            r = await app.client.post(url, headers=hdrs, data=lpd)
            
            status = 'UNKNOWN'
            reason = ''
            if r.status_code == 200:
                c = r.content
                m = None
                for off in [0, 64] + list(range(128)):
                    try:
                        temp = app.thunderFF_pb2.MajorLoginRes()
                        temp.ParseFromString(c[off:])
                        if temp.region and temp.token:
                            m = temp
                            break
                    except Exception:
                        pass
                
                if m and m.token:
                    status = 'OK_ACTIVE'
                else:
                    status = 'BANNED'
                    for txt in [b'Protection Bypass', b'Bypass', b'ban', b'suspension']:
                        if txt in c:
                            reason = txt.decode()
            else:
                status = f"HTTP_{r.status_code}"
            
            print(f"{uid} | {nick:<15} | Status: {status} {reason}")
            results[uid] = {'status': status, 'reason': reason, 'nick': nick}
        except Exception as e:
            print(f"{uid} | {nick:<15} | ERROR: {e}")
            results[uid] = {'status': 'ERROR', 'error': str(e), 'nick': nick}

    print('\n--- SUMMARY ---')
    active = [u for u, v in results.items() if v.get('status') == 'OK_ACTIVE']
    banned = [u for u, v in results.items() if v.get('status') == 'BANNED']
    other = [u for u, v in results.items() if u not in active and u not in banned]
    print(f"Total: {len(results)}")
    print(f"Active/Safe ({len(active)}): {active}")
    print(f"Banned/Suspended ({len(banned)}): {banned}")
    if other:
        print(f"Other ({len(other)}): {other}")

if __name__ == '__main__':
    asyncio.run(check_all())
