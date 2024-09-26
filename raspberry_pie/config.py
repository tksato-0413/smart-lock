

from dataclasses import dataclass, field
from utils import dump_params
from argparse import ArgumentParser


@dataclass(frozen=True)
class Parameters:
    """
    プログラム全体を通して共通のパラメータを保持するクラス．
    ここにプロジェクト内で使うパラメータを一括管理する．
    """
    args: dict = field(default_factory=lambda: {})  # コマンドライン引数
    run_date: str = ''  # 実行時の時刻
    git_revision: str = ''  # 実行時のプログラムのGitのバージョン
    external_server_url: str='' # 外部サーバーのURL(ローカルIPアドレス)
    wait_time: int = 10  # カードの読み込み待ち時間。単位は秒


def common_args(parser: 'ArgumentParser'):
    """
    コマンドライン引数を定義する関数．
    Args:
        parser (:obj: ArgumentParser):
    """
    parser.add_argument("-p", "--parameters", help="パラメータ設定ファイルのパスを指定．デフォルトはNone", type=str, default=None)
    return parser


if __name__ == "__main__":
    dump_params(Parameters(), './', partial=True)
