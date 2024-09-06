import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
from pathlib import Path

# テスト対象のモジュールをインポート
from motor_control import control, unlock, lock, other_order

class TestMotorControl(unittest.TestCase):
    def setUp(self):
        # パラメータ設定（テストで使用するモックデータ）
        self.params = {
            "servo_pin": 18,
            "freq": 50,
            "unlock": {"angle": 0, "duty_cycle": 2.5},
            "lock": {"angle": 90, "duty_cycle": 7.5}
        }
        self.valid_angle = 0  # 解錠時の角度
        self.invalid_angle = 45  # 無効な角度（施錠も解錠もされていない状態）

    @patch('builtins.open', new_callable=mock_open, read_data="0")  # モックファイルの内容を角度0に設定
    @patch('motor_control.GPIO')  # GPIOライブラリをモック化
    @patch('motor_control.utils.set_logging')  # ログ出力をモック化
    def test_control_unlock(self, mock_logging, mock_gpio, mock_file):
        """
        'unlock' 指令を受けて鍵を解錠するテスト
        """
        logger_mock = MagicMock()
        mock_logging.return_value = logger_mock
        
        # テストの実行
        result = control("unlock", self.params)
        
        # 結果の確認
        self.assertEqual(result, "Already unlocked.")
        logger_mock.info.assert_called_with("現在の鍵の角度：0 °C")  # ログに正しく出力されているか

    @patch('builtins.open', new_callable=mock_open, read_data="90")  # 現在の角度が90度で施錠されている状態
    @patch('motor_control.GPIO')  # GPIOライブラリをモック化
    @patch('motor_control.utils.set_logging')  # ログ出力をモック化
    def test_control_lock(self, mock_logging, mock_gpio, mock_file):
        """
        'lock' 指令を受けて鍵を施錠するテスト
        """
        logger_mock = MagicMock()
        mock_logging.return_value = logger_mock
        
        # テストの実行
        result = control("lock", self.params)
        
        # 結果の確認
        self.assertEqual(result, "Already locked.")
        logger_mock.info.assert_called_with("現在の鍵の角度：90 °C")

    @patch('builtins.open', new_callable=mock_open, read_data="45")  # 角度が45度で解錠/施錠中間の状態
    @patch('motor_control.GPIO')  # GPIOライブラリをモック化
    @patch('motor_control.utils.set_logging')  # ログ出力をモック化
    def test_other_order(self, mock_logging, mock_gpio, mock_file):
        """
        無効な指令が与えられた場合の例外処理のテスト
        """
        logger_mock = MagicMock()
        mock_logging.return_value = logger_mock
        
        # テストの実行
        result = control("invalid_order", self.params)
        
        # 結果の確認
        self.assertEqual(result, "Locking")
        logger_mock.warning.assert_called_with("無効なメッセージが入力されました。\n 内容：invalid_order")

if __name__ == '__main__':
    unittest.main()
