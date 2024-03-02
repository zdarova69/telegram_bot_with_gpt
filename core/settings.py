from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int

@dataclass
class Settings:
    bots: Bots

def get_settings(token: str, adm_id:int):
    
    return Settings(
        bots=Bots(
            bot_token=token,
            admin_id=adm_id
        )
    )
settings = get_settings()
print(settings)