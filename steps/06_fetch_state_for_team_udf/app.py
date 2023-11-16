from snowflake.snowpark import Session

def main(session: Session, team_name: str) -> str:
    session.use_schema('NFL_SPONSOR')
    team_state_df = session.table("TEAM_STATE_LOOKUP")
    state_code_row = team_state_df.filter(team_state_df["TEAM_NAME"] == team_name).select("STATE_CODE").collect()
    return state_code_row[0]["STATE_CODE"] if state_code_row else None


if __name__ == '__main__':
    # Add the utils package to our path and import the snowpark_utils function
    import os, sys
    current_dir = os.getcwd()
    parent_parent_dir = os.path.dirname(os.path.dirname(current_dir))
    sys.path.append(parent_parent_dir)

    from utils import snowpark_utils
    session = snowpark_utils.get_snowpark_session()

    if len(sys.argv) > 1:
        print(main(session, *sys.argv[1:]))  # type: ignore
    else:
        print(main(session))  # type: ignore

    session.close()