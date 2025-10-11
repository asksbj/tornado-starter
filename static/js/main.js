// 主要的JavaScript功能

document.addEventListener('DOMContentLoaded', function() {
    console.log('Tornado Web应用已加载');
    
    // 初始化工具提示
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // 显示欢迎消息
    showWelcomeMessage();
});

function showWelcomeMessage() {
    // 可以在这里添加欢迎消息的显示逻辑
    console.log('欢迎使用Tornado Web应用！');
}

// 通用API调用函数
async function callApi(url, method = 'GET', data = null) {
    try {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            }
        };
        
        if (data) {
            options.body = JSON.stringify(data);
        }
        
        const response = await fetch(url, options);
        const result = await response.json();
        
        return {
            success: response.ok,
            data: result,
            status: response.status
        };
    } catch (error) {
        return {
            success: false,
            error: error.message
        };
    }
}

// 显示加载状态
function showLoading(element) {
    element.classList.add('loading');
    element.innerHTML = '<span class="spinner"></span>加载中...';
}

// 隐藏加载状态
function hideLoading(element, originalText) {
    element.classList.remove('loading');
    element.innerHTML = originalText;
}

// 显示通知
function showNotification(message, type = 'info') {
    // 创建通知元素
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.zIndex = '9999';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // 3秒后自动消失
    setTimeout(() => {
        if (notification.parentNode) {
            notification.parentNode.removeChild(notification);
        }
    }, 3000);
}

