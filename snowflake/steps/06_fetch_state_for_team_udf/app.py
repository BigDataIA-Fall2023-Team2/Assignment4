from utils import get_snowpark_session
import sys

def main(team_name: str) -> str:
    session = get_snowpark_session()
    team_state_df = session.table("TEAM_STATE_LOOKUP")
    state_code_row = team_state_df.filter(team_state_df["TEAM_NAME"] == team_name).select("STATE_CODE").collect()
    return state_code_row[0]["STATE_CODE"] if state_code_row else None

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(*sys.argv[1:]))  # type: ignore
    else:
        print(main())