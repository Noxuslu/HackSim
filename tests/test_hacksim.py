from hacksim import generate_report

def test_report_format():
    ip = "192.168.1.1"
    report = generate_report(ip)
    assert "Hedef" in report
    assert ip in report
    assert "Bulunan açıklar" in report
  
