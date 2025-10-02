
document.addEventListener('DOMContentLoaded', function () {
    const toggle = document.querySelector('.nav-toggle');
    const navList = document.getElementById('primary-navigation');

    if (!toggle || !navList) return;

    function closeMenu() {
        navList.classList.remove('show');
        toggle.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
    }

    function toggleMenu() {
        const isOpen = navList.classList.toggle('show');
        toggle.classList.toggle('active');
        toggle.setAttribute('aria-expanded', String(isOpen));
    }

    // 點擊漢堡選單切換
    toggle.addEventListener('click', function(e) {
        e.stopPropagation();
        toggleMenu();
    });

    // 點擊選單項目時關閉選單（在手機版）
    navList.addEventListener('click', function(e) {
        if (window.innerWidth <= 800 && e.target.tagName === 'A') {
            closeMenu();
        }
    });

    // 點擊頁面其他地方關閉選單
    document.addEventListener('click', function(e) {
        if (window.innerWidth <= 800 && !navList.contains(e.target) && !toggle.contains(e.target)) {
            closeMenu();
        }
    });

    // 按 ESC 鍵關閉選單
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && window.innerWidth <= 800) {
            closeMenu();
        }
    });

    // 視窗大小改變時處理選單狀態
    window.addEventListener('resize', function() {
        if (window.innerWidth > 800) {
            // 回到桌面版時移除手機版相關類別
            navList.classList.remove('show');
            toggle.classList.remove('active');
        }
    });
});