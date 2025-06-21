import pytest
import os
from core.session.session_manager import SessionManager

@pytest.mark.asyncio
async def test_session_save_load():
    manager = SessionManager("test_session")
    test_data = {"user_id": 123, "auth_key": "test_key"}
    
    await manager.save_session(test_data)
    assert os.path.exists("sessions/test_session.session")
    
    loaded_data = await manager.load_session()
    assert loaded_data == test_data
    
    os.remove("sessions/test_session.session")
