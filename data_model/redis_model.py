

def serialize_localgovt(localgovt) :
    return {
        "id": localgovt.id,
        "name": localgovt.name,
        "created_at": localgovt.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
        "states_id": localgovt.states_id
    }
