"""便利な関数群"""
from __future__ import annotations  # Python 3.7, 3.8はこの記述が必要
import subprocess
import json
from datetime import datetime
import os
from dataclasses import asdict
from typing import Any
from logging import getLogger, StreamHandler, FileHandler, Formatter, DEBUG, INFO, WARNING, ERROR, CRITICAL, Logger


def get_git_revision() -> str:
    """
    現在のGitのリビジョンを取得
    Returns:
         str: revision ID
    """
    cmd = "git rev-parse HEAD"
    revision = subprocess.check_output(cmd.split())  # 現在のコードのgitのリビジョンを取得
    return revision.decode()


def setup_params(args_dict: dict[str, Any], path: str = None) -> dict[str, Any]:
    """
    コマンドライン引数などの辞書を受け取り，実行時刻，Gitのリビジョン，jsonファイルからの引数と結合した辞書を返す．
    
        Args:
            args_dict (dict): argparseのコマンドライン引数などから受け取る辞書
            path (str, optional): パラメータが記述されたjsonファイルのパス

        Returns:
            dict: args_dictと実行時刻，Gitのリビジョン，jsonファイルからの引数が結合された辞書．
                構造は {'args': args_dict, 'git_revision': <revision ID>, 'run_date': <実行時刻>, ...}．
    """
    run_date = datetime.now()
    git_revision = get_git_revision()  # Gitのリビジョンを取得

    param_dict = {}
    if path:
        param_dict = json.load(open(path, 'r'))  # jsonからパラメータを取得
    param_dict.update({'args': args_dict})  # コマンドライン引数を上書き
    param_dict.update({'run_date': run_date.strftime('%Y%m%d_%H%M%S')})  # 実行時刻を上書き
    param_dict.update({'git_revision': git_revision})  # Gitリビジョンを上書き
    return param_dict


def dump_params(params: 'Parameters', outdir: str, partial: bool = False) -> None:
    """
    データクラスで定義されたパラメータをjson出力する関数
    Args:
        params (:ogj: `Parameters`): パラメータを格納したデータクラス
        outdir (str): 出力先のディレクトリ
        partial (bool, optional): Trueの場合，args，run_date，git_revision を出力しない，
    """
    params_dict = asdict(params)  # デフォルトパラメータを取得
    if os.path.exists(f'{outdir}/parameters.json'):
        raise Exception('"parameters.json" is already exist. ')
    if partial:
        del params_dict['args']  # jsonからし指定しないキーを削除
        del params_dict['run_date']  # jsonからし指定しないキーを削
        del params_dict['git_revision']  # jsonからし指定しないキーを削
    with open(f'{outdir}/config.json', 'w') as f:
        json.dump(params_dict, f, indent=4)  # デフォルト設定をファイル出力


def set_logging(result_dir: str, file_name: str = "log", 
                stdout_log_level: str ="INFO", fileout_log_level: str ="DEBUG") -> Logger:
    """
    ログを標準出力とファイルに書き出すよう設定する関数．

        Args:
            result_dir (str): ログの出力先
            stdout_log_level: str = "INFO": 標準出力(ターミナル)のログレベル
            fileout_log_level: str = "DEBUG": ファイル出力のログレベル
        Returns:
            設定済みのrootのlogger
    
        Example: 
        >>> # logger = logging.getLogger(__name__)
        >>> # set_logging(result_dir)
        >>> # logger.info('log message...')
    """
    logger = getLogger()
    # 実際に出力されるのレベルは、handlerとfile_handlerでそれぞれ指定するので、
    # 以下では、最も出力レベルが低いDEBUGにしておく。
    logger.setLevel(DEBUG)  # 全体のログレベル
    
    # formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # ログのフォーマット
    formatter = Formatter('%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s')  # ログのフォーマット

    # 標準出力へのログ出力設定
    handler = StreamHandler()
    handler.setLevel(stdout_log_level.upper()) # ターミナル出力ログレベル
    handler.setFormatter(formatter)  # フォーマットを指定
    logger.addHandler(handler)
    
    # ファイル出力へのログ出力設定
    file_handler = FileHandler(f'{result_dir}/{file_name}.log', 'a+')  # ログ出力ファイル
    file_handler.setLevel(fileout_log_level.upper()) # ファイル出力ログレベル
    file_handler.setFormatter(formatter)  # フォーマットを指定
    logger.addHandler(file_handler)
    
    return logger


def update_json(json_file: str, input_dict: dict[str, Any]) -> None:
    """jsonファイルをupdateするプログラム
        import json が必要
    Args:
        json_file (str): jsonファイルのpath
        input_dict (dict): 追加もしくは更新したいdict
    """
    with open(json_file) as f:
        df = json.load(f)

    df.update(input_dict)

    with open(json_file, 'w') as f:
        json.dump(df, f, indent=4)
